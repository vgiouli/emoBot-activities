import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional


INPUT_FILE = "activities_export_20260405_205448.json"
OUTPUT_FILE = "sentence_ordering_training_dataset.json"


def normalize_whitespace(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def safe_json_loads(value: Any) -> Any:
    if isinstance(value, (list, dict)):
        return value
    if not isinstance(value, str):
        return None
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return None


def extract_instruction(
    activity: Dict[str, Any],
    first_sentence: str,
    last_sentence: str,
    language: str = "de"
) -> str:
    """
    Prefer existing anchor/question text where available.
    Otherwise create a clean default instruction.
    """
    questions = activity.get("questions", [])
    question_text = ""
    anchor_text = ""

    if questions:
        question_text = normalize_whitespace(questions[0].get("question", ""))
        anchor_text = normalize_whitespace(questions[0].get("anchor", ""))

    combined = " ".join([anchor_text, question_text]).strip()

    if combined and ("beginnt" in combined.lower() or "endet" in combined.lower()):
        return combined

    if language.lower() == "de":
        return (
            f"Bringen Sie die Sätze in die richtige Reihenfolge. "
            f'Der Text beginnt mit „{first_sentence}“ und endet mit „{last_sentence}“.'
        )
    elif language.lower() == "el":
        return (
            f"Βάλτε τις προτάσεις στη σωστή σειρά. "
            f'Το κείμενο αρχίζει με «{first_sentence}» και τελειώνει με «{last_sentence}».'
        )
    else:
        return (
            f"Put the sentences in the correct order. "
            f'The text begins with "{first_sentence}" and ends with "{last_sentence}".'
        )


def build_source_text(first_sentence: str, ordered_middle: List[str], last_sentence: str) -> str:
    all_sentences = [first_sentence] + ordered_middle + [last_sentence]
    return " ".join(normalize_whitespace(s) for s in all_sentences if normalize_whitespace(s))


def convert_activity(activity: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if activity.get("activity_type") != "sentence_ordering":
        return None

    questions = activity.get("questions", [])
    if not questions:
        return None

    answer_raw = questions[0].get("answer")
    answer_items = safe_json_loads(answer_raw)
    if not isinstance(answer_items, list) or not answer_items:
        return None

    # Validate and sort by correct_position
    cleaned_items = []
    for item in answer_items:
        if not isinstance(item, dict):
            continue
        label = normalize_whitespace(str(item.get("letter", "")))
        text = normalize_whitespace(item.get("text", ""))
        pos = item.get("correct_position")

        if not label or not text or not isinstance(pos, int):
            continue

        cleaned_items.append({
            "label": label,
            "text": text,
            "correct_position": pos
        })

    if not cleaned_items:
        return None

    cleaned_items.sort(key=lambda x: x["correct_position"])

    text_meta = activity.get("text", {}) or {}
    language = str(activity.get("language", "de")).lower()
    level = text_meta.get("cefr_level")
    topic = text_meta.get("topic")
    title = text_meta.get("title")

    description = normalize_whitespace(activity.get("description", ""))

    # Try to extract first/last sentence from description if present
    first_sentence = None
    last_sentence = None

    m1 = re.search(r"beginnt mit [„\"](.+?)[“\"]", description)
    m2 = re.search(r"endet mit[: ]*[„\"](.+?)[“\"]", description)

    if m1:
        first_sentence = normalize_whitespace(m1.group(1))
    if m2:
        last_sentence = normalize_whitespace(m2.group(1))

    # Fallback if description does not contain anchors
    if not first_sentence:
        # Some entries only store a fragment; use the first ordered item as fallback only if necessary
        first_sentence = "[MISSING_FIRST_SENTENCE]"
    if not last_sentence:
        last_sentence = "[MISSING_LAST_SENTENCE]"

    ordered_middle = [item["text"] for item in cleaned_items]
    source_text = build_source_text(first_sentence, ordered_middle, last_sentence)

    # Preserve shuffled order as it appears in original answer array, not sorted order
    shuffled_items = []
    for item in answer_items:
        if not isinstance(item, dict):
            continue
        label = normalize_whitespace(str(item.get("letter", "")))
        text = normalize_whitespace(item.get("text", ""))
        pos = item.get("correct_position")
        if not label or not text or not isinstance(pos, int):
            continue
        shuffled_items.append({
            "label": label,
            "text": text,
            "original_position": pos + 1  # +1 because position 1 is the fixed first sentence
        })

    # Correct solution order by label according to correct_position
    solution = [
        item["label"]
        for item in sorted(
            [
                {
                    "label": normalize_whitespace(str(x.get("letter", ""))),
                    "correct_position": x.get("correct_position")
                }
                for x in answer_items
                if isinstance(x, dict)
                and isinstance(x.get("correct_position"), int)
                and normalize_whitespace(str(x.get("letter", "")))
            ],
            key=lambda x: x["correct_position"]
        )
    ]

    instruction = extract_instruction(activity, first_sentence, last_sentence, language)

    record = {
        "task": "generate_sentence_ordering_exercise",
        "language": language,
        "level": level,
        "topic": topic,
        "source_title": title,
        "source_text": source_text,
        "sentences": [first_sentence] + ordered_middle + [last_sentence],
        "exercise": {
            "instruction": instruction,
            "first_sentence": first_sentence,
            "last_sentence": last_sentence,
            "items": shuffled_items,
            "solution": solution
        },
        "source_metadata": {
            "activity_id": activity.get("id"),
            "question_id": questions[0].get("id"),
            "notes": activity.get("notes"),
            "status": activity.get("status")
        }
    }

    return record


def main():
    input_path = Path(INPUT_FILE)
    output_path = Path(OUTPUT_FILE)

    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    activities = data.get("activities", [])
    converted = []
    skipped = []

    for activity in activities:
        try:
            result = convert_activity(activity)
            if result is not None:
                converted.append(result)
            else:
                skipped.append(activity.get("id"))
        except Exception as e:
            skipped.append({
                "activity_id": activity.get("id"),
                "error": str(e)
            })

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(converted, f, ensure_ascii=False, indent=2)

    print(f"Converted records: {len(converted)}")
    print(f"Skipped records: {len(skipped)}")
    if skipped:
        print("Some skipped activity ids/errors:")
        print(json.dumps(skipped[:20], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

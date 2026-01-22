# emoBot Language Learning and Testing Activities

This repository contains a suite of datasets of **Language Learning and Testing Activities in German**, created within the **emoBot project**.  
The dataset is designed for research and development in **language learning technologies**, **reading comprehension**, and **educational NLP**, including applications such as intelligent tutoring systems, conversational agents, and assessment tools.

---

## DE-MC: German Multiple-Choice Questions Dataset: Overview

- **Language:** German (DE)
- **Task type:** Multiple-choice questions
- **Total activities:** 370
- **Competences covered:**
  - Reading
  - Vocabulary (in selected activities)
- **Content domains:** everyday life, society, education, culture, work, migration, entertainment, sports, travel, family
- **Status labels:** approved, pending_review
- **Source inspiration:** Authentic learning materials (e.g. DW Learn German)

Each activity is linked to a short text and contains multiple questions with:
- one correct answer
- one or more distractors

---

## File Description

### `data/DE-MC-20260122.json`

A JSON file containing the full dataset, exported on **2026-01-22**.

Top-level structure:
- `export_date`
- `total_activities`
- `filters_applied`
- `activities` (list)

---

## Data Structure (Simplified)

```json
{
  "id": 677,
  "activity_type": "multiple_choice",
  "language": "DE",
  "linguistic_competence": ["Reading"],
  "description": "...",
  "status": "pending_review",
  "text": {
    "id": 999,
    "title": "Frauen im Kölner Karneval",
    "topic": "society",
    "cefr_level": null
  },
  "questions": [
    {
      "question": "Eine Mitgliedschaft in einem Traditionskorps ist möglich für …",
      "answer": "Männer.",
      "distractors": [
        { "text": "Frauen." },
        { "text": "Frauen und Männer." }
      ]
    }
  ]
}

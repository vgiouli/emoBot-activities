# emoBot Language Learning and Testing Activities

This repository contains a suite of datasets of **Language Learning and Testing Activities in German**, created within the **emoBot project**.  
The dataset is designed for research and development in **language learning technologies**, **reading comprehension**, and **educational NLP**, including applications such as intelligent tutoring systems, conversational agents, and assessment tools.

---

## MCQ-de: German Multiple-Choice Questions Dataset: Overview

- **Language:** German (DE)
- **Task type:** Multiple-choice questions
- **Total multiple-choice questions:** 370
- **Competences covered:**
  - Reading
  - Vocabulary (in selected activities)
- **Content domains:** everyday life, society, education, culture, work, migration, entertainment, sports, travel, family
- **Status labels:** approved, pending_review
- **Source inspiration:** Authentic learning materials (e.g. DW Learn German)

Each activity is linked to a short text and contains multiple questions:
- one correct answer
- one or more distractors

---

## File Description

### `data/DE/MCQ-de.json`

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
          "id": 1028,
          "question_order": 2,
          "anchor": "Im Text steht: \"Der Begriff stammt eigentlich aus dem popkulturellen Kontext, es ging darum, den Anschluss an das soziale und kulturelle Umfeld nicht zu verlieren. Wer »dabei« sein will, muss heutzutage ständig informiert und damit online sein. Erst während der Pandemie merkten viele plötzlich, wie gut es tut, auch einmal zu entschleunigen und einfach nur bei sich selbst zu sein.\"",
          "question": "Welche Alternative gibt die Bedeutung von \"zu entschleunigen und einfach nur bei sich selbst zu sein.\" richtig wieder?",
          "answer": "den Lebensrhythmus zu verlangsamen und seine innere Mitte zu finden.",
          "distractors": [
            {
              "text": "langsam zu machen und die Gesellschaft anderer zu suchen.",
              "order": 1
            },
            {
              "text": "mit den anderen mitzuhalten, aber gleichzeitig seine innere Ruhe zu bewahren.",
              "order": 2
            }
          ]
        },

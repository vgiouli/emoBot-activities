# emoBot Language Learning and Testing Activities


This repository contains a suite of datasets of **Language Learning and Testing Activities**, developed within the **emoBot project**.

The dataset is designed to support research and development in:

- **Language Learning Technologies**
- **Reading Comprehension**
- **Educational NLP**

Typical applications include:

- Intelligent Tutoring Systems (ITS)
- Conversational Agents / Chatbots
- Automated Assessment and Evaluation Tools

---

## Activity Types

The dataset includes the following activity types:

### 1. Fill-in-the-Blanks

With three subtypes:

- **Shared List**  
  A common pool of options is provided for all blanks. Currently, the .dev split is available.

- **Individual Options**  
  Each blank has its own set of candidate answers --> dataset not ready yet.

- **No Distractors**  --> dataset not ready yet.
  Learners provide answers without predefined options.

---

### 2. Sentence Ordering

Learners are given:

- The **first** and **last** sentence of a text are (optionally) provided
- A set of **shuffled intermediate sentences**

The task for the bot is to (a) create a short text, (b) split the text into sentences and label them, (c) optionally) set the first and last sentences as fixed, (d) suffle the non-fixed and present them to the user, and (e) correct the users.

---

### 3. Multiple-Choice Questions (not available yet)

Standard multiple-choice items with one or more correct answers, used for:

- Reading comprehension
- Vocabulary and grammar assessment

---

## Dataset Structure

The dataset is split into:

- `train`
- `dev`
- `test`

Each split is designed to support:

- Model training
- Validation and tuning
- Final evaluation

---

## Use Cases

This dataset can be used for:

- Training NLP models for **educational applications**
- Evaluating **reading comprehension systems**
- Developing **adaptive learning environments**
- Building **LLM-based language tutors**

---

## Project Context

This work is part of the **emoBot project**, which focuses on:

- Emotion-aware conversational agents
- Language learning support through AI
- Personalized educational experiences

---

## License

*(Add your license here, e.g. MIT / CC BY-NC / etc.)*

---

## Contact

*(Optional: add contact info or project website)*


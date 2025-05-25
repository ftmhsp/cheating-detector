````markdown
# 🧠 Cheating Detection System

This project is a university-level final project that detects cheating in online exams using semantic text similarity and response timing. It consists of a backend API with FastAPI and a frontend submission form in HTML.

---

## 👨‍💻 Features

- Submit student answers and time per question
- Detect cheating based on:
  - Semantic similarity of text answers (using Sentence Transformers)
  - Suspiciously close response times
- Clean and minimal frontend interface
- SQLite database for storing responses
- Modular and scalable codebase

---

## 🧩 Tech Stack

- **Backend**: FastAPI + Uvicorn
- **AI**: Sentence-Transformers (`paraphrase-multilingual-MiniLM-L12-v2`)
- **Database**: SQLite
- **Frontend**: HTML + JavaScript (Vanilla)
- **Language**: Python 3.10+

---

## 📦 Installation

1. Clone this repository  
2. Navigate to the project folder  
3. Install dependencies:

```bash
pip install -r requirements.txt
````

---

## 🚀 Running the Project

### ▶️ Start the API server:

```bash
uvicorn main:app --reload
```

### 🌐 Run the frontend form (in another terminal):

```bash
python -m http.server 5500
```

Then open [http://localhost:5500/index.html](http://localhost:5500/index.html) in your browser.

---

## 📤 Submit Answers

* Fill the form as student S1 and S2 with similar answers and times
* Press “Submit Answers”
* Then click “Analyze Cheating” to see results

---

## 📊 Sample Output

```
👯 Text Similarity Detected between S1 and S2 in Q1 (83%)
⏱️ Time Similarity Detected (difference: 1 second)
```

---

## 👥 Team Members

* 👤 fatemeh hosseinpour (Backend, Database, API)
* 👤 mobina alidoosti (Frontend, Cheating Analysis)

---

## 🏷️ Notes

* Code is modular and scalable
* Branches and commits used to separate responsibilities
* API can be extended for live exams, dashboards, or logging
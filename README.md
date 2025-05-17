# Interactly-task-Kushal-Desai
# Candidate Matching System

This project is a candidate matching system that utilizes OpenAI's GPT-3.5-turbo model, Streamlit for the user interface, MySQL for data storage, and NLTK for natural language processing. The system allows users to input a job description and fetch the best-matched candidates from a database based on the job description details.

# 🔍 Candidate Matching System using GPT-3.5, Streamlit, and NLP

A smart, AI-powered system that matches candidates to job descriptions using **OpenAI's GPT-3.5-turbo**, **Streamlit** for the interactive UI, **MySQL** for data storage, and **NLTK** for natural language processing.

This project demonstrates how generative AI and classic NLP techniques can be combined to solve a real-world HR challenge: **finding the best-suited candidates from a resume database based on a given job description**.

---

## 🚀 Features

- ✨ **GPT-3.5 Matching Logic**: Uses OpenAI's GPT-3.5-turbo model to evaluate semantic similarity between job descriptions and candidate resumes.
- 🔎 **Smart Filtering**: Extracts relevant entities (skills, experience, etc.) from text using NLP for pre-filtering before GPT ranking.
- 🖥️ **Streamlit UI**: A simple, clean web interface to paste job descriptions and view top-matching candidates.
- 🧠 **Natural Language Processing**: Leveraging NLTK for tokenization, stopword filtering, and keyword extraction.
- 💾 **MySQL Database**: Stores and fetches candidate data (resumes, contact info, skills) efficiently.
- 📊 **Ranking System**: Candidates are ranked based on how well their resumes align with the job requirements.

---

## 🧱 Tech Stack

| Tool/Tech     | Role                                      |
|---------------|-------------------------------------------|
| 🧠 OpenAI GPT-3.5 | Semantic matching + ranking logic          |
| 🧪 NLTK        | Text preprocessing & keyword extraction   |
| 🧰 Streamlit   | Web-based interface for user interaction  |
| 🛢 MySQL       | Persistent storage of resumes and metadata |
| 🐍 Python      | Core programming language                 |

---

## 📷 Interface Preview

*Coming Soon:* Add screenshots or a short GIF demo here showing the UI in action.

---

## 🧠 How It Works

1. **User inputs a job description** in the Streamlit app.
2. **NLP processing** (via NLTK) extracts key terms (skills, experience, roles).
3. **MySQL query** fetches candidate profiles from the database.
4. **GPT-3.5** ranks candidates by how closely their profile matches the job description.
5. **Top matches** are displayed in a clean, ranked list.

---

## 🛠️ Setup & Installation

```bash
# Clone the repo
git clone https://github.com/your-username/candidate-matcher

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run app.py





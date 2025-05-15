# 🎬 IMDb Movie Review Sentiment Analyzer (3-Class) + Emojis

An interactive chatbot that analyzes movie reviews and classifies them as **Positive**, **Neutral**, or **Negative**, with a modern Gradio interface and emoji-enhanced user experience.

> Built with `scikit-learn`, `nltk`, and `Gradio`, this project combines classic ML with modern UI for an engaging sentiment analysis tool.

---

## 🚀 Live Demo

🎯 Try it out on Hugging Face Spaces:  
🔗 [https://huggingface.co/spaces/drashti3001/IMDB_Analyser](https://huggingface.co/spaces/drashti3001/IMDB_Analyser)

---

## 📸 Screenshot

![App Screenshot](https://huggingface.co/spaces/drashti3001/IMDB_Analyser/resolve/main/demo.png) <!-- Optional: replace with your actual screenshot path -->

---

## 💡 Features

- ✅ **3-Class Sentiment Classification**: Positive, Neutral, Negative
- 🤖 **Logistic Regression + TF-IDF** model for real-time review analysis
- 🧠 **IMDb movie review dataset** via NLTK
- 💬 **Emoji-enhanced interaction** with clickable buttons
- 🖥️ **Modern Gradio UI** with live input and chat history
- 🌐 **Hosted on Hugging Face Spaces** (public and free)

---

## 🛠️ Tech Stack

| Tool           | Purpose                        |
|----------------|-------------------------------|
| Python         | Programming Language           |
| scikit-learn   | ML pipeline (TF-IDF + LR)      |
| NLTK           | IMDb dataset for training       |
| Gradio         | Chat interface frontend        |
| Hugging Face   | Live app deployment            |

---

## 📦 Installation Instructions

### 🔧 Requirements
- Python 3.7+
- pip

### ▶️ Setup & Run

```bash
git clone https://github.com/drashti3001/IMDB_Analyser.git
cd IMDB_Analyser
pip install -r requirements.txt
python app.py

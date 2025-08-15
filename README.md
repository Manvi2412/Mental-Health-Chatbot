# Mindful — Mental Health Chatbot

> Kind, empathetic, and simple emotional support.  
> **Disclaimer:** This chatbot is not a substitute for professional help. If you are in crisis, please reach out to your local suicide prevention helpline immediately.

---

## Overview

Mindful is an **AI-powered mental health chatbot** built with **Streamlit** that offers supportive and empathetic responses based on the user's emotional state.  
It detects mood (Positive, Negative, Neutral) using **Natural Language Processing (NLP)** and provides helpful, non-repetitive, and caring messages to encourage open conversation.

This project is designed for **resume showcase** purposes, demonstrating skills in:
- Python development
- Natural Language Processing
- Sentiment analysis
- Streamlit web app deployment
- User interface design

---

## Features

-  **Real-time Chat** — Interactive conversation between user and bot.
-  **Mood Detection** — Identifies whether the sentiment is positive, negative, or neutral.
-  **Mood Trends** — Optional visualization of mood trends over time.
-  **Non-repetitive, empathetic responses** for better engagement.
-  **Crisis Detection** — If the user expresses suicidal thoughts, the bot provides **emergency helpline contacts**.
-  **Deployable on Streamlit Cloud** for instant online access.

---

## Tech Stack

- **Frontend & Backend:** [Streamlit](https://streamlit.io/)
- **Language:** Python
- **NLP & Sentiment Analysis:** NLTK / Scikit-learn
- **Data Handling:** Pandas
- **Deployment:** Streamlit Cloud / Localhost

---

## Screenshots

### Chat Interface
![Chat Interface] <img width="554" height="432" alt="image" src="https://github.com/user-attachments/assets/b03af346-f33f-471d-8403-d7e99ed65dda" />


---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
```
### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### 3. Run the Application
```bash
streamlit run app.py
```
The chatbot will be available at:
http://localhost:8501

### Folder Structure
mental-health-chatbot/
│
├── app.py            # Streamlit UI & app logic
├── chatbot.py        # Chatbot logic, mood detection & responses
├── requirements.txt  # Project dependencies
├── README.md         # Project documentation

### Mood Detection Logic
Preprocessing:
Lowercasing
Removing stopwords
Tokenization
Sentiment Analysis:
Classifies messages into Positive, Negative, or Neutral.
Response Generation:
Selects an empathetic reply based on mood category.
Crisis keywords trigger suicide prevention message.

### Crisis Helpline
If you are feeling suicidal or are in emotional distress, please contact:
India: AASRA — 91-9820466726
USA: 988 Suicide and Crisis Lifeline — Call or Text 988
UK: Samaritans — 116 123 (freephone)

### Future Improvements
Add multilingual support
Integrate with a transformer-based conversational model
Store chat history in a database for analysis
Personalize responses based on user profile

### License
This project is licensed under the MIT License.

### Author

### Manvi Taneja
manvitaneja70952@gmail.com




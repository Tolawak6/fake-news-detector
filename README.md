# 📰 Fake News Detection App

A machine learning-powered web application that detects whether a given news article is **Fake** or **Real** using Natural Language Processing and Scikit-learn.

---

## 🚀 Features

- Text-based fake news classification using Logistic Regression + TF-IDF
- Flask-powered REST API and web interface
- Real-time prediction with confidence score
- Clean HTML UI for manual testing
- Fully open-source and extendable

---

## 🔍 Model Overview

- **Algorithm:** Logistic Regression
- **Vectorizer:** TF-IDF (word-level)
- **Dataset:** [Kaggle Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- **Labels:**
  - `0` → Real News
  - `1` → Fake News

---

## 📁 Project Structure

fake-news-detector/
├── app.py # Flask backend
├── model/
│ └── fake_news_model.joblib # Saved model pipeline
├── templates/
│ └── index.html # Web UI
├── static/
│ └── style.css # CSS styles
├── requirements.txt # Python dependencies
└── test/
└── test_api.py # API test script


---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/fake-news-detector.git
   cd fake-news-detector

2.**Create and activate a virtual environment**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Ensure your model file is in place**
Save the trained pipeline as fake_news_model.joblib under the model/ directory

**Run the App**
python app.py

📬 API Usage
Endpoint
POST /api/predict

JSON Body
{
  "text": "Your news article content goes here"
}
Response

{
  "label": "Fake",
  "confidence": 0.9325
}

**Run Test Script**
python test/test_api.py


Author
Tolawak Merga
GitHub: Tolawak6
linkdin: [Tolawak Merga](https://www.linkedin.com/in/tolawak-merga)
Instagram: (https://www.instagram.com/t_o_l_a_w_a_k)
Telegram: https://t.me/tolawakMerga

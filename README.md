# 📦 Customer Query Classification System

#### Live Link : https://customer-query-classifier.onrender.com

## 🌟 Project Overview

This project implements a Machine Learning (ML) solution to automatically classify incoming customer support queries for an e-commerce platform (simulated using a Flipkart dataset). The primary goal is to triage messages instantly, directing them to the appropriate support queue based on their content.

The system is deployed as a lightweight web application using the **Flask** framework.

### Key Classification Categories:
- **🔁 Return/Refund Related**
- **📩 Other** (e.g., Order Status, Feedback, Offers, etc.)

---

## 💻 Tech Stack

| Component         | Technology       | Role |
|----------|------------|------|
| **Backend Framework** | **Python, Flask** | Handles routing, application logic, and serving the frontend. |
| **Model** | **Scikit-learn (Logistic Regression)** | The trained ML model used for classification. |
| **Text Preprocessing** | **TfidfVectorizer** | Converts raw text messages into numerical features. |
| **Model Serialization** | **Joblib** | Used to save and load the trained model components (`.pkl` files). |
| **Deployment Server** | **Gunicorn** | Production-ready WSGI server required for cloud hosting. |
| **Frontend** | **HTML, CSS (Jinja Templating)** | The user interface for entering queries and viewing results. |

---

## 📂 Project Structure
Customer Query Classification/
├── app.py # Main Flask application logic
├── templates/
│ └── index.html # Frontend HTML/CSS template
├── model.pkl # Serialized trained Logistic Regression model
├── vectorizer.pkl # Serialized TfidfVectorizer instance
├── label_encoder.pkl # Serialized LabelEncoder
├── requirements.txt # List of Python dependencies for production
└── Procfile # Deployment configuration for Gunicorn/Heroku/Render


---

## 🛠️ Setup and Installation (Local)

Follow these steps to run the application on your local machine:

### 1. Clone the Repository
```bash
git clone <YOUR_REPOSITORY_URL>
cd "Customer Query Classification"
```

2. Create a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# .\venv\Scripts\activate  # On Windows
```

3. Install Dependencies
```
pip install -r requirements.txt
```

5. Run the Application
```
python app.py
or
py app.py
```

5. Access the App
Open your browser and visit:
```
👉 http://127.0.0.1:5000/
```

### 🧠 Machine Learning Details
The core classification logic was developed in the included ML_notebook.ipynb.

Model Type: Logistic Regression (Binary Classification)

Feature Extraction: TF-IDF Vectorization

Performance: (Optional – Add metrics such as accuracy, e.g., ~92%)

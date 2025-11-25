import joblib
from flask import Flask, render_template, request

# --- 1. Load Models ---
try:
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    label_encoder = joblib.load("label_encoder.pkl")
    print("Models, Vectorizer, and Label Encoder loaded successfully.")
except FileNotFoundError:
    print("Error: One or more model files (model.pkl, vectorizer.pkl, label_encoder.pkl) not found.")
    # Exit or handle the error gracefully
    exit()

# --- 2. Initialize Flask App ---
app = Flask(__name__)

# --- 3. Define Routes ---

@app.route('/')
def home():
    """Renders the main prediction page."""
    # The 'result' is passed as None initially or after a fresh load
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the prediction request from the web form."""
    if request.method == 'POST':
        # Get the text input from the form
        user_input = request.form['customer_query']

        if not user_input or user_input.strip() == "":
            prediction_label = "Please enter a customer query to classify."
            prediction_status = "warning"
        else:
            try:
                # 1. Transform the input text
                X_input = vectorizer.transform([user_input])

                # 2. Make the prediction
                prediction = model.predict(X_input)[0]

                # 3. Get the human-readable label
                label = label_encoder.inverse_transform([prediction])[0]
                
                # Based on the logic in your Streamlit app:
                # 1 suggests 'Return/Refund Related'
                if label == 1:
                    prediction_label = f"Return/Refund Related 🔁"
                    prediction_status = "success"
                else:
                    prediction_label = f"Other (e.g., order, feedback, offers) 📩"
                    prediction_status = "info"

            except Exception as e:
                # Catch any error during prediction (e.g., model issue)
                prediction_label = f"An error occurred: {e}"
                prediction_status = "error"

        # Render the template again, passing the results
        return render_template('index.html', 
                               user_query=user_input, 
                               prediction_label=prediction_label,
                               prediction_status=prediction_status)

# --- 4. Run the App ---
if __name__ == '__main__':
    # Set debug=True for development to see errors immediately
    app.run(debug=True)
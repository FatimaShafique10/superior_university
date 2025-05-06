from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained SVC model
with open('svc_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [int(x) for x in request.form.values()]
        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        result = "Approved" if prediction == 1 else "Not Approved"
        return render_template('index.html', prediction_text=f"Loan Prediction: {result}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

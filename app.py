from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load Model
model = joblib.load("model.pkl")

@app.route('/predict', methods=['GET', 'POST'])  # 🟢 GET aur POST dono allow kar diye
def predict():
    if request.method == 'GET':
        return "API Running! Use POST request to send data.", 200  # Agar GET request aaye to simple message bhejo
    
    # POST request ke liye
    data = request.get_json()
    x_value = np.array([[data['X']]])
    prediction = model.predict(x_value)[0]
    
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

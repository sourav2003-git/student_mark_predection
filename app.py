from flask import Flask, request, jsonify
import pickle

app = Flask(_name_)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return "Student Marks Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.json['hours'])
    prediction = model.predict([[hours]])
    return jsonify({"Predicted Marks": prediction[0]})

if _name_ == "_main_":
    app.run(debug=True)

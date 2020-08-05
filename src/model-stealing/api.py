from flask import Flask, jsonify
from flask import request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    df = pd.DataFrame(json_)
    prediction = model.predict(df)
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    model = pickle.load(open('model_rf.pkl', 'rb'))
    app.run(port=8080)
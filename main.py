import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify


from modules.insurance_model import InsuranceModel

app = Flask(__name__)

@ app.route('/')
def index():
    return "API Modeling"


@ app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    x =  InsuranceModel().runModel(df, typed='single')

    return jsonify({
        "status": "Predicted",
        "result": x
    })
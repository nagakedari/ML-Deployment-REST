from flask_restful import Resource, reqparse
from flask import request, jsonify, Blueprint, current_app, jsonify
import pandas as pd

predictor_api = Blueprint('predictor_api', __name__)

class Predictor(Resource):

    def predict(self, model, payload):
        data = pd.json_normalize(payload)
        prediction = model.predict(data)
        predicted_strength = {
            'predicted_strength': prediction[0]
        }
        return jsonify(predicted_strength), 200
    

model_predictor = Predictor()

@predictor_api.route("/predict", methods=['PUT'], )
def predict():
    payload = request.get_json(force=True)
    model = current_app.config['model']
    return model_predictor.predict(model, payload)
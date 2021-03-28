from flask import Flask
from flask_restful import Resource, Api, reqparse
import pickle
from predictor import predictor_api

app = Flask(__name__)
app.register_blueprint(predictor_api, url_prefix='/model')
api = Api(app)

model = None

def load_model():
    global model
    with open('concrete_strength_trained_model.pkl', 'rb') as m:
        model = pickle.load(m)
        
print('Running {}'.format(__name__))
if __name__ == '__main__':
    load_model() # load the model on flask start
    app.config['model'] = model
    app.run(host='0.0.0.0', port=80)
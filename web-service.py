import tensorflow as tf
from tensorflow import keras
import json
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def runner():
    return app.send_static_file('home.html')

# uses the speed value given and based off the model takes power value from it and returns the power as a
# String
@app.route('/power', methods=['POST'])
def parse_request():
    data = request.data
    returnedData = json.loads(data)
    windSpeed = float(returnedData['speed'])
    model = tf.keras.models.load_model('modelpowerproduction.h5')
    prediction = model.predict([windSpeed])
    predictionOneDimen = prediction.flatten()
    print(predictionOneDimen[0])
    return str(predictionOneDimen[0])

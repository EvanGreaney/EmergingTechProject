import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
import json
from flask import Flask, jsonify,request
app = Flask(__name__)

@app.route('/')
def runner():
    return app.send_static_file('home.html')

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


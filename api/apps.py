from django.apps import AppConfig
from django.conf import settings
from tensorflow import keras
import os
from tensorflow.python.lib.io import file_io

BUCKET_NAME = os.getenv("BUCKET_NAME")


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

class BatikPredictionModelConfig(AppConfig):
    name = 'predictionAPI'
    model_file = file_io.FileIO('gs://{}/ML-model/batik_model_final.h5'.format(BUCKET_NAME), mode='rb')

    # Save the model file to a local temporary file
    temp_local_model_file = '/tmp/batik_model_temp.h5'
    with open(temp_local_model_file, 'wb') as temp_file:
        temp_file.write(model_file.read())

    # Load the model using keras.models.load_model
    loaded_model = keras.models.load_model(temp_local_model_file)

    model = keras.models.load_model(temp_local_model_file)

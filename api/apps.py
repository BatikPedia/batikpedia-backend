from django.apps import AppConfig
from django.conf import settings
from tensorflow import keras
import os
from google.cloud import storage

BUCKET_NAME = "batikpedia-apigateway-bucket-staging"

storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

class BatikPredictionModelConfig(AppConfig):
    name = 'predictionAPI'
    model_file = bucket.blob('ML-model/batik_model_final.h5')
    model = keras.models.load_model(model_file.name)

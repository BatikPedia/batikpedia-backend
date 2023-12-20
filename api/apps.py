from django.apps import AppConfig
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow import keras
import os


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

class BatikPredictionModelConfig(AppConfig):
    name = 'predictionAPI'
    MODEL_FILE = os.path.join(settings.ML_MODELS, "batik_model.h5")
    model = keras.models.load_model(MODEL_FILE)
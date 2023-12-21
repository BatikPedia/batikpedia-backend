from api.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from .apps import BatikPredictionModelConfig
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .auth_utils import *
from keras.preprocessing.image import img_to_array
from PIL import Image

import numpy as np
import tensorflow as tf


@api_view(http_method_names=['GET'])
def healthz(request):
    return Response(status=200, message='Server is running.')


class AuthenticateView(APIView):
    def get(self, request):
        auth_class = JWTAuthentication()

        # get the token first
        token = get_request_header_authorization(request)
        if token is None:
            return Response({'detail' : 'You haven\'t logged in'}, status=status.HTTP_401_UNAUTHORIZED)

        # check the token's validity
        user = auth_class.get_user(validated_token=auth_class.get_validated_token(token))
        if user is None:
            return Response({'detail' : 'Your credential token is either invalid or expired'}, status=status.HTTP_401_UNAUTHORIZED)

        # finally, return the user
        serializer = UserSerializer(user)
        user_data = serializer.data
        return Response(data=dict(user_data), status=200)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.create(validated_data=validated_data)
            return Response(message='User successfully created! Log in to continue!', status=status.HTTP_201_CREATED,data=validated_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# Create your views here.
class PredictBatikView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        ## Load ML model.
        batik_model = BatikPredictionModelConfig.model

        # Get file image from JSON
        file = request.FILES['image']
        file_name = file.name

        pillow_image = Image.open(file)                     # Convert file to Pillow image    
        pillow_image = pillow_image.resize((256, 256))      # Resize
        pillow_image = pillow_image.convert("L")            # Greyscale
        
        image_np_array = img_to_array(pillow_image)         # Convert Pillow image to numpy array
        image_np_array = image_np_array / 255               # Normalize
        image_np_array = np.expand_dims(image_np_array, axis=0)

        # Remember, output of this CNN is the z value
        try:
            prediction_logits = batik_model.predict(image_np_array)
        except Exception as e:
            print(e)

        # Convert z value to probability using softmax function
        prediction_probs = tf.nn.softmax(prediction_logits)

        # Get predicted labels
        prediction_label_value = np.argmax(prediction_probs, 1)

        # Converting prediction label values to label names
        if (prediction_label_value == 0):
            prediction_label = "kawung"
        elif (prediction_label_value == 1):
            prediction_label = "mega-mendung"
        elif (prediction_label_value == 2):
            prediction_label = "parang"
        elif (prediction_label_value == 3):
            prediction_label = "sekar-jagad"
        elif (prediction_label_value == 4):
            prediction_label = "tambal"
        else:
            prediction_label = "unknown"

        # Prepare response.
        response_data = {
            'file_name' : file_name,
            'batik_pred': prediction_label
        }
        
        response_message = 'Successfully predicted an image'
        response_status = status.HTTP_200_OK

        response = Response(
            data=response_data, 
            status=response_status, 
            message=response_message)

        return response


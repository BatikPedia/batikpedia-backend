from api.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .auth_utils import *


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
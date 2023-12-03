from api.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(http_method_names=['GET'])
def healthz(request):
    return Response(status=200, message='Server is running.')
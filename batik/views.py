from django.shortcuts import render
from rest_framework.decorators import api_view
from api.response import Response
from .services import *

@api_view(['GET'])
def list_all_batik_view(request):
    result = list_all_batik()
    return Response(data=result, message="nih")

@api_view(['GET'])
def get_batik_by_id_view(request):
    result = get_batik_by_id('wmSVCHei1hnksB4uUCU5')
    return Response(data=result, message="nih")
    
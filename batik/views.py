from django.shortcuts import render
from rest_framework.decorators import api_view
from api.response import Response
from .services import *

@api_view(['GET'])
def list_all_batik_view(request):
    query = request.query_params
    if 'province' in query:
        result = list_batik_by_province(query['province'])
    else:
        result = list_all_batik()
    return Response(data=result, message="Successfully fetched all batik informations", status=200)

@api_view(['GET'])
def get_batik_by_id_view(request, batik_id):
    result = get_batik_by_id(batik_id)
    if result is None:
        return Response(message="Batik ID not found!", status=404)
    return Response(data=result, message="Batik found!", status=200)


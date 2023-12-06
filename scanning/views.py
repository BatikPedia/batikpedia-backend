from api.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound, ValidationError
from . import models

@api_view(http_method_names=['GET', 'POST'])
def ScanningListCreateAPIView(request):
    '''List/Create API view for scanning.'''
    try:
        if request.method == 'GET':
            docs = models.Scanning().get(many=True)
            return Response(status=200, message='OK', data=docs)
        if request.method == 'POST':
            instance = models.Scanning(**request.data)
            new_doc = instance.save()
            return Response(status=201, message='Created', data=new_doc)
        return Response(status=405, message='Method not allowed')
    except NotFound as e:
        return Response(status=404, message=str(e))
    except Exception as e:
        return Response(status=400, message=str(e))

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def ScanningRetrieveUpdateDestroyAPIView(request, uuid):
    '''Retrieve/Update/Delete API view for scanning.'''
    try:
        if request.method == 'GET':
            doc = models.Scanning(uuid=uuid).get()
            return Response(status=200, message='OK', data=doc)
        if request.method == 'PUT':
            instance = models.Scanning(uuid=uuid, **request.data)
            updated_doc = instance.update()
            return Response(status=200, message='OK', data=updated_doc)
        if request.method == 'DELETE':
            models.Scanning(uuid=uuid).delete()
            return Response(status=204, message='No content')
        return Response(status=405, message='Method not allowed')
    except NotFound as e:
        return Response(status=404, message=str(e))
    except Exception as e:
        return Response(status=400, message=str(e))
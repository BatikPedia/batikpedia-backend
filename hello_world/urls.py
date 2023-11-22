from django.urls import path
from .views import *

urlpatterns = [
    path('/', hello_world_response, name='hello'),
]
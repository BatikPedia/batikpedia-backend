from django.urls import path
from .views import *

urlpatterns = [
    path('all/', list_all_batik_view, name='all_batik'),
    path('id/<str:batik_id>', get_batik_by_id_view, name='batik_by_id')
]
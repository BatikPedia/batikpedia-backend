from django.urls import path
from .views import *

urlpatterns = [
    path('all/', list_all_batik_view.as_view(), name='all_batik'),
    path('id/', get_batik_by_id_view.as_view(), name='batik_by_id')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ScanningListCreateAPIView, name='list_scanning'),
    path('<str:uuid>/', views.ScanningRetrieveUpdateDestroyAPIView, name='detail_scanning'),
]

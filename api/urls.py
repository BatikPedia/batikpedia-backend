from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import *

urlpatterns = [
    # Health Check
    path('healthz/', healthz, name='healthz'),

    # Auth Endpoints
    path('auth', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Returns the user object
    path('token/verify/', AuthenticateView.as_view(), name='check_auth'), 

    # registration endpoint
    path('auth/register', RegisterView.as_view(), name='register'), 

    path('batik/', include('batik.urls')),
    path('scanning/', include('scanning.urls')),

    # Batik model prediction endpoint.
    path('predict_batik/', PredictBatikView.as_view(), name='predict_batik')
]

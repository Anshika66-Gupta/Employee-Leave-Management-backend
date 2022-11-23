from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework_simplejwt.views import TokenVerifyView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('nice',views.Verifyss.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # path('login/', views.MyTokenObtainPairView.as_view()),
]
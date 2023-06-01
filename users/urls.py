from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
urlpatterns = [
    path('login/',  views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('emailcheck/',  views.DuplicateCheck, name="emailcheck"),
    path('namecheck/',  views.NameCheck, name="namecheck"),
    
]
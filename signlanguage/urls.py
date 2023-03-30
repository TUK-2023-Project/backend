from django.urls import path
from . import views
from .views import get_file_url

urlpatterns = [
    #path('upload/', ImageUploader.as_view(), name="upload"),
    path('upload/', views.get_file_url, name="upload"),
    #path('testuser/', views.testuser, name="testuser"),
    path('info/', views.get_info, name="info"),
    path('three/', views.three_random, name="three_random"),
    
    
]


from django.urls import path
from . import views
from .views import get_file_url

urlpatterns = [
    #path('upload/', ImageUploader.as_view(), name="upload"),
    path('upload/', views.get_file_url, name="upload"),
    
    
]


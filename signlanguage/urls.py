from django.urls import path
from . import views
from .views import get_file_url
from .views import SignView
urlpatterns = [
    #path('upload/', ImageUploader.as_view(), name="upload"),
    path('upload/', views.get_file_url, name="upload"),
    #path('testuser/', views.testuser, name="testuser"),
    path('info/', views.get_info, name="info"),
    path('three/', SignView.as_view(), name="three_random"),
    
    
]


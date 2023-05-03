from django.urls import path
from . import views
from .views import printdd

urlpatterns = [
    #path('upload/', ImageUploader.as_view(), name="upload"),
    path('upload/', views.printdd, name="printdd"),

    
    
]


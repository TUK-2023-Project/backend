from django.urls import path
from . import views
from .views import add_note

urlpatterns = [
    #path('upload/', ImageUploader.as_view(), name="upload"),
    path('add/', views.add_note, name="add"),
    path('delete/', views.delete_note, name="delete"),
    path('list/', views.show_list_note, name="list"),
    


    
    
]


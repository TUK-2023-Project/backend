from django.urls import path
from .views import RankView

app_name = 'ranks'

urlpatterns = [
    path('', RankView.as_view(), name='rank-list'),
    path('save/', RankView.as_view(), name='rank-save'),
]
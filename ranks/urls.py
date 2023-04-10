from django.urls import path
from .views import RankView, UserRankView

app_name = 'ranks'

urlpatterns = [
    path('', RankView.as_view(), name='rank-list'),
    path('save/', RankView.as_view(), name='rank-save'),
    path('self/', UserRankView.as_view(), name='self'),
]
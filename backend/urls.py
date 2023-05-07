from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/signlanguage/', include('signlanguage.urls')),
    path('api/v1/users/',include('users.urls')),
    path('api/v1/ranks/',include('ranks.urls')),
    path('api/v1/incorrect/',include('incorrect_note.urls')),
     

]

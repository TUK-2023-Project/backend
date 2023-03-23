from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signlanguage/', include('signlanguage.urls')),
    path('api/v1/users/',include('users.urls')),
     

]

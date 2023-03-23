from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signlanguage/', include('signlanguage.urls')),
    path('users/',include('users.urls')),
     

]

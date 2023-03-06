from django.urls import re_path

from . import comsumers

websocket_urlpatterns = [
    re_path(r'ws/signlanguage/', comsumers.SignLanguageConsumer.as_asgi()),
]
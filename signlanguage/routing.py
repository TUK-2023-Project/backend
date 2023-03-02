# from django.urls import re_path

# from .. import comsumers

# websocket_urlpatterns = [
#     re_path('ws/signLanguage/', comsumers.RealTimeVideoConsumer),
# ]


# # from channels.routing import ProtocolTypeRouter, URLRouter
# # from django.urls import path
# # from .. import comsumers

# # application = ProtocolTypeRouter({
# #     'websocket': URLRouter([
# #         path('ws/signlanguage/', comsumers.RealTimeVideoConsumer),
# #     ]),
# # })

# # chatapp/routing.py

from django.urls import re_path

from . import comsumers

websocket_urlpatterns = [
    re_path(r'ws/signlanguage/', comsumers.SignLanguageConsumer.as_asgi()),
]
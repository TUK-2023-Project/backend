# """
# ASGI config for signlan project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
# """

# # import os

# # from django.core.asgi import get_asgi_application

# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# # application = get_asgi_application()

# # mysite/asgi.py
# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import chat.routing

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })


# application = ProtocolTypeRouter({
#     'websocket': URLRouter([
#         path('ws/signlanguage/', consumers.SignLanguageConsumer.as_asgi()),
#     ]),
# })


import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
application = get_default_application()
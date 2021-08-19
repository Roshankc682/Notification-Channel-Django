import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from core_channel.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_channel.settings')

application = get_asgi_application()

# first protocol and then routers
application = get_asgi_application()

ws_patterns = [
    path('ws/test/',TestConsumer),
    path('ws/hello/',HelloChannel)
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from socket_notification_app.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socket_notification_app.settings')

application = get_asgi_application()

# first protocol and then routers
application = get_asgi_application()

ws_patterns = [
    path('ws/firstchannel/',TestConsumer),
    path('ws/secondchannel/',AnotherChannel),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/drawing/', consumers.DrawingConsumer.as_asgi()),  # WebSocket endpoint
]

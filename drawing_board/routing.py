from django.urls import path
from .consumers import DrawingConsumer

websocket_urlpatterns = [
    path("ws/drawing/", DrawingConsumer.as_asgi()),
]

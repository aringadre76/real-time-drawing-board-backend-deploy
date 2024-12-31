from django.urls import path
from . import consumers

# Django requires `urlpatterns` for URL routing
urlpatterns = [
    path('drawing/', consumers.DrawingConsumer.as_asgi()),  # WebSocket endpoint
]

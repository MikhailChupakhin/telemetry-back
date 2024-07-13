# C:\Users\user1\PycharmProjects\Telemetry-emulator\main\websocket_app\routing.py
from django.urls import path
from .consumers import DataConsumer

websocket_urlpatterns = [
    path('ws/data/', DataConsumer.as_asgi()),
]

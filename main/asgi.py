"""
ASGI config for back-app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import socketio
import asyncio

import example_data.examples

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back-app.settings')

sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*',
    logger=False,
    engineio_logger=False
)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        socketio.ASGIApp(sio)
    ),
})

client_tasks = {}


@sio.event
async def connect(sid, environ):
    print(f"New client connected: {sid}")
    await sio.emit('message', {'data': 'Connected successfully!'}, room=sid)

    task = asyncio.create_task(send_telemetry(sid))
    client_tasks[sid] = task


@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")


async def send_telemetry(sid):
    try:
        while True:
            if not sio.manager.is_connected(sid, '/'):
                print(f"Client {sid} no longer connected, stopping timestamp sending")
                break

            ''' Emulation !'''
            telemetry_data = {
                'runtime': example_data.examples.generate_random_runtime_data(),
                'parameters': example_data.examples.example_parameters_data
            }

            await sio.emit('timestamp', data=telemetry_data, room=sid)
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print(f"Task for client {sid} was cancelled")
    finally:
        print(f"Finished sending timestamps to client {sid}")


@sio.on('*')
async def catch_all(event, sid, data):
    print(f"Caught event: {event}, sid: {sid}, data: {data}")

# uvicorn back-app.asgi:application --host 0.0.0.0 --port 8000 --reload


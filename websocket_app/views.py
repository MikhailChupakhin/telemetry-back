from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_data_to_websocket(data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'data_channel',  # Имя группы канала
        {
            'type': 'send_data',  # Название метода в DataConsumer
            'data': data,
        }
    )

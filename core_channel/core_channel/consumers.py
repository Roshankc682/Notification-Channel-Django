from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):

    def connect(self, *args,**kwargs):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected from channel '}))

    def receive(self,text_data):
        print(text_data)
        self.send(text_data=json.dumps({'message': 'we got your message'}))
        pass

    def disconnect(self, *args,**kwargs):
        print("disconnected")
        # pass


class HelloChannel(WebsocketConsumer):
    
    def connect(self, *args,**kwargs):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected from channel '}))

    def receive(self,text_data):
        print(text_data)
        self.send(text_data=json.dumps({'message': 'we got your message'}))
        pass

    def disconnect(self, *args,**kwargs):
        print("disconnected")
        # pass
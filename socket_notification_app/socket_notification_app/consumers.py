from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):

    def connect(self, *args,**kwargs):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected to first channel '}))

    def receive(self,text_data):
        print(text_data)
        self.send(text_data=json.dumps({'message': 'first channel got message'}))
        pass

    def disconnect(self, *args,**kwargs):
        print("disconnected from first")
        # pass

    def send_notification(self,event):
        print("send notification to first channel")
        date = json.loads(event.get('value'))
        print(event)
        self.send(text_data=json.dumps(date))




class AnotherChannel(WebsocketConsumer):

      def connect(self, *args,**kwargs):
        self.room_name = "first_consumer"
        self.room_group_name = "first_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected to second channel '}))

        def receive(self,text_data):
            print(text_data)
            self.send(text_data=json.dumps({'message': 'second channel got message'}))
            pass

        def disconnect(self, *args,**kwargs):
            print("disconnected from second")
            # pass

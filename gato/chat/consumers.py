from channels.generic import websockets


class ChannelConsumer(websockets.JsonWebsocketConsumer):

    strict_ordering = False

    def connection_groups(self, **kwargs):
        return ["chat"]

    def receive(self, message, **kwargs):
        self.send(message)

from channels import Group
from channels.generic import websockets

import json


# def ws_add(message):
#     message.reply_channel.send({"accept": True})
#     Group("chat").add(message.reply_channel)
#
#
# def ws_message(message):
#     print(message.content)
#     mes = json.loads(message.content['text'])
#     Group("chat").send({
#         "text": "[%s] %s" % (
#             mes['username'],
#             mes['message']
#         )
#     })
#
#
# def ws_disconnect(message):
#     Group("chat").discard(message.reply_channel)


class ChannelConsumer(websockets.JsonWebsocketConsumer):

    strict_ordering = False

    def connection_groups(self, **kwargs):
        return ["chat"]

    def receive(self, message, **kwargs):
        self.send(message)

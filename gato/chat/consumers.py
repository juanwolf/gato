from channels import Group
import json


def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)


def ws_message(message):
    print(message.content)
    mes = json.loads(message.content['text'])
    Group("chat").send({
        "text": "[%s] %s" % (
            mes['username'],
            mes['message']
        )
    })


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)

from channels.routing import route

from chat import consumers


channel_routing = [
    route("websocket.receive", consumers.ws_message),
    route("websocket.connect", consumers.ws_add),
    route("websocket.disconnect", consumers.ws_disconnect)
]

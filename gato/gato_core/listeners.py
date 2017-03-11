import logging as log


class EventListenerManager:
    event_listeners = {}

    @property
    def categories(self):
        return self.event_listeners.keys()

    def add_category(self, category):
        self.debug("Creating new event listener category %s" % category)
        self.event_listeners[category] = {}

    def register(self, category, event_listener):
        class_name = event_listener.__class__.__name__
        if category not in self.event_listeners:
            log.error(
                "Unknown category %s, did you call add_category?" % category
            )
        self.event_listeners[category][class_name] = event_listener

    def unregister(self, category, event_listener):
        if category not in self.event_listeners:
            log.error(
                "Unknown category %s, not unregistering the event_listener" %
                category
            )
        del self.event_listeners[event_listener.__class__.__name__]


class GenericEventListener:
    category = None

    def pre():
        """
        Action occuring before the main action.
        """
        pass

    def post():
        """
        Action occuring after the main action.
        """
        pass

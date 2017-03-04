import timezone

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)


class Room(models.Model):
    name = models.CharField(length=50)
    label = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages")
    user = models.CharField(length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

from django.contrib.auth.models import User
from django.db import models

class ChatRoom(models.Model):
    user1 = models.ForeignKey(User, related_name='chatrooms1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='chatrooms2', on_delete=models.CASCADE)

class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

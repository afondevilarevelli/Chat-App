from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# class Chat(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# class Message(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     text = models.TextField()

#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="messages")
#     chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name="messages")

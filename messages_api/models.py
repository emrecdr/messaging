from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    sender = models.ForeignKey(User, related_name='user_sender', on_delete = models.CASCADE, blank = False, null = True)
    receiver = models.ForeignKey(User, related_name='user_receiver', on_delete = models.CASCADE, blank = False, null = True)

    def __str__(self):
        return self.message
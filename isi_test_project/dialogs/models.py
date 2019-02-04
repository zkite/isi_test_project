from django.db import models
from isi_test_project.settings import AUTH_USER_MODEL


class Thread(models.Model):
    participants = models.ManyToManyField(AUTH_USER_MODEL, related_name='threads')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField()


class Message(models.Model):
    text = models.TextField(blank=True)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    created = models.DateField(auto_now_add=True)

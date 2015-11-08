from django.db import models
from django.utils import timezone


class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.username

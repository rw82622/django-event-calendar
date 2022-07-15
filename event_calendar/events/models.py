from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class TheUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=50,
        unique=True
    )
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    starts_at = models.DateTimeField(default=timezone.now)
    ends_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(TheUser, on_delete=models.CASCADE)

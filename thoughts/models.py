from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
      return f" {self.content}"
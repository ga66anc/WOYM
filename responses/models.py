from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Response(models.Model):
    thought = models.ForeignKey('thoughts.Thought',
                                 related_name='thoughts',
                                 on_delete=models.CASCADE)
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    body = models.CharField(max_length=100)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
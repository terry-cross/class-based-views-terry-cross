from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    body = RichTextField(blank=True, null=True)
    # body = models.CharField(max_length=100)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    header_image = models.ImageField(upload_to="images/", null=True, blank=True)
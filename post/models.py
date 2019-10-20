from django.db import models
from accounts.models import MyUser
from django.conf import settings
from django.utils import timezone
import uuid


# Create your models here.
class Post(models.Model):
    post_pic = models.ImageField(blank=False, null=False, upload_to='posts')
    post_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user_liked')
    post_date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return str(self.pk)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(blank=False, null=False, max_length=1000)
    comment_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True)
    comment_date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.comment

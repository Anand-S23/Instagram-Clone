from django.db import models
from django.conf import settings
from django.utils import timezone
from post.models import Post

# Create your models here.
class LikeAct(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reciving_like')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='acting_like')
    act = models.TextField(default="liked")
    liked_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.from_user} {self.act} post from {self.to_user}.'


class FollowAct(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reciving_follow')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='acting_follow')
    act = models.TextField(default="followed") 
    followed_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.from_user} {self.act} {self.to_user}.'

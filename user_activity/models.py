from django.db import models
from django.conf import settings
from django.utils import timezone
from post.models import Post

# Create your models here.
class Act(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reciving')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='acting')
    act = models.TextField()
    act_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        if self.act == 'followed':
            return f'{self.from_user} {self.act} you.'
        else:
            return f'{self.from_user} {self.act} your post.'

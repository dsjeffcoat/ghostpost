from django.db import models
from django.utils import timezone

# Create your models here.


class GhostPost(models.Model):
    is_boast = models.BooleanField(default=True)
    post = models.CharField(max_length=280)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    time_submitted = models.DateTimeField(default=timezone.now)
    sec_key = models.CharField(max_length=6)

    def __str__(self):
        return self.post

    def total_score(self):
        return self.upvote - self.downvote

from datetime import datetime
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.now)
    text = models.TextField()

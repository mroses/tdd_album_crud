from django.db import models

class Album(models.Model):
    title = models.CharField(max_length = 60)
    artist = models.CharField(max_length = 60)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



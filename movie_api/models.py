from django.db import models



class MovieData(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    runtime = models.CharField(max_length=10)
    poster = models.URLField()
    description = models.TextField()

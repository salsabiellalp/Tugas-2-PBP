from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField(max_length=200)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
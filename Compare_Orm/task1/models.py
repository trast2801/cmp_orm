from django.db import models

# Create your models here.



class Cinema(models.Model):
    name = models.CharField(max_length=200)
    movie_duration = models.CharField(max_length=50)
    movie_year = models.IntegerField(default=1900)
    genres = models.CharField(max_length=50, default=" ")
    countries = models.CharField(max_length=40, default=" ")


    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=200)
    review = models.TextField()

    def __str__(self):
        return self.name


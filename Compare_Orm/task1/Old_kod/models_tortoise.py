from tortoise import Tortoise, fields, models, run_async
from tortoise.models import Model
from tortoise import fields

class T_Review(Model):
    #id = fields.IntField(primary_key=True)
    review = fields.TextField()
    name = fields.CharField(max_length=256)
# Create your models here.
    class Meta:
        table = "task1_review"

class T_Cinema(Model):
    #id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=256)
    movie_duration = fields.CharField(max_length=256)
    movie_year = fields.IntField()
    genres = fields.CharField(max_length=50)
    countries = fields.CharField(max_length=40)

    class Meta:
        table = "task1_cinema"


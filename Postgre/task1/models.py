from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance =models.DecimalField(decimal_places=2, max_digits=7)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100) # названиеигры
    cost = models.DecimalField(decimal_places=2, max_digits=7) # цена(DecimalField)
    size = models.DecimalField(decimal_places=2, max_digits=7) # размер файловигры(DecimalField)
    description = models.TextField()# описание(неограниченное кол - во  текста)
    age_limited = models.BooleanField(default= False) # - ограничение возраста 18 + (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='buyer')

    def __str__(self):
        return self.title

class Psg_user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.username

class Psg_book(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    id_user = models.ForeignKey(Psg_user, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
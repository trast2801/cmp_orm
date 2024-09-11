
from tortoise.models import Model
from tortoise.fields import IntField, CharField, TextField


class T_Review(Model):
    id = IntField(pk=True)
    name = CharField(max_length=100)
    review = TextField()

    class Meta:
        table = "task1_review"
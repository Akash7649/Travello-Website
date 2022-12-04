from django.db import models

# Create your models here.

#this is used without Postgres database
# class Destination:
#     id:int
#     name:str
#     img:str
#     desc:str
#     price:int
#     offer: True


#this is used when we use postgres database
class Destination(models.Model):

    name = models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

from django.db import models

# Create your models here.
class Funko(models.Model):
    name= models.CharField(max_length= 128)
    numero = models.IntegerField()
    collection = models.CharField(max_length= 128)
    is_backlight = models.BooleanField(default= False)
    
class User(models.Model):
    name= models.CharField(max_length= 128)
    funkos= models.ForeignKey(Funko, on_delete=models.PROTECT)

    
    
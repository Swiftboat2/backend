from django.db import models

# Create your models here.


class Skins(models.Model):
    name = models.CharField(max_length=128)
    float = models.IntegerField()
    rarity = models.CharField(max_length=128)
    pattern = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.float} - {self.name}'
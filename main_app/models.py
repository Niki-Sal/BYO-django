from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    plant = models.CharField(max_length=100)
    instruction = models.CharField(max_length=250)

    def __str__(self):
        return self.name
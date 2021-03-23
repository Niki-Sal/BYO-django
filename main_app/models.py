from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    plant = models.CharField(max_length=100)
    instruction = models.CharField(max_length=250)

    def __str__(self):
        return self.name

CARES = (
    ('W','Watering'),
    ('F', 'Use fertilizer'),
    ('S', 'Change soil'),
    ('P', 'Change plant pot')
)

class gardening(models.Model):

    date = models.DateField()
    care = models.CharField(
        max_length = 1,
        choices = CARES,
        default = CARES[0][0]
    )
    plant = models.ForeignKey(Plant, on_delete = models.CASCADE)

    def __str__ (self):
        return f"{self.get_care_display()} on {self.date}"

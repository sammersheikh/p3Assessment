from django.db import models

# Create your models here.

WIDGET = (
    ('1', 'Widget1'),
    ('2', 'Widget2'),
    ('3', 'Widget3'),
    ('4', 'Widget4'),
    ('5', 'Widget5'),
)

class Stuff(models.Model):
    widget = models.CharField(
        max_length=10,
        choices = WIDGET,
        default = WIDGET[0][0]
    )
    quantity = models.IntegerField(default=1)

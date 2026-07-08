from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TEMP_CHOICES = [
        ('C', 'Celsius'),
        ('F', 'Fahrenheit'),
    ]

    temp_unit = models.CharField(
        max_length=1,
        choices=TEMP_CHOICES,
        default='C'
    )

    def __str__(self):
        return self.username
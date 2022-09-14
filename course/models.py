from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    ratings = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

from django.db import models
from basis.models import BasisModel


class Person(BasisModel):
    name = models.CharField(max_length=100)

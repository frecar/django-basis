from django.db import models
from basis.models import BasisModel, PersistentModel, TimeStampModel


class BasisPerson(BasisModel):
    name = models.CharField(max_length=100)


class TimeStampPerson(TimeStampModel):
    name = models.CharField(max_length=100)


class PersistentPerson(PersistentModel):
    name = models.CharField(max_length=100)

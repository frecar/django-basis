from basis.models import BasisModel, PersistentModel, TimeStampModel
from django.db import models


class BasisPerson(BasisModel):
    name = models.CharField(max_length=100)


class TimeStampPerson(TimeStampModel):
    name = models.CharField(max_length=100)


class PersistentPerson(PersistentModel):
    name = models.CharField(max_length=100)

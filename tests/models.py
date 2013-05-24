from django.db import models
from basis.models import BaseModel


class Person(BaseModel):
    name = models.CharField(max_length="100")
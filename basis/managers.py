from django.db import models
from .compat import DJANGO16


if DJANGO16:
    class BasisModelManager(models.Manager):
        def get_queryset(self):
            return super(BasisModelManager, self).get_queryset().filter(deleted=False)
else:
    class BasisModelManager(models.Manager):
        def get_query_set(self):
            return super(BasisModelManager, self).get_query_set().filter(deleted=False)

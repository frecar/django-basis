from django.db import models
from .compat import DJANGO16


class _BasisModelManager(models.Manager):
    def create(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)
        instance = super(_BasisModelManager, self).create(*args, **kwargs)
        instance.created_by = user
        instance.updated_by = user
        return instance


if DJANGO16:
    class BasisModelManager(_BasisModelManager):
        def get_queryset(self):
            return super(BasisModelManager, self).get_queryset().filter(deleted=False)
else:
    class BasisModelManager(_BasisModelManager):
        def get_query_set(self):
            return super(BasisModelManager, self).get_query_set().filter(deleted=False)

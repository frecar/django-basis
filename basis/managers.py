from django.db import models
from .compat import DJANGO16


if DJANGO16:
    class PersistentModelManager(models.Manager):
        def get_queryset(self):
            return super(PersistentModelManager, self).get_queryset().filter(deleted=False)
else:
    class PersistentModelManager(models.Manager):
        def get_query_set(self):
            return super(PersistentModelManager, self).get_query_set().filter(deleted=False)


class BasisModelManager(PersistentModelManager):
    def create(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)
        kwargs['created_by'] = user
        kwargs['updated_by'] = user
        instance = super(BasisModelManager, self).create(*args, **kwargs)
        return instance

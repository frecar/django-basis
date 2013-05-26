from django.db import models


class BasisModelManager(models.Manager):
    def get_query_set(self):
        return super(BasisModelManager, self).get_query_set().filter(deleted=False)
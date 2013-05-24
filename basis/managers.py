from django.db import models


class BaseModelManager(models.Manager):
    def get_query_set(self):
        return super(BaseModelManager, self).get_query_set().filter(deleted=False)
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from .managers import BasisModelManager


class BasisModel(models.Model):
    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=datetime.now(), auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), null=True, default=None, related_name="%(class)s_created")

    updated_at = models.DateTimeField(default=datetime.now(), auto_now=True)
    updated_by = models.ForeignKey(get_user_model(), null=True, default=None, related_name="%(class)s_updated")

    objects = BasisModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        if 'current_user' in kwargs:
            if not self.id:
                self.created_by = kwargs['current_user']

            self.updated_by = kwargs['current_user']

        super(BasisModel, self).save()

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def restore(self, *args, **kwargs):
        self.deleted = False
        self.save()
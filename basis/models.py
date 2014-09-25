from datetime import datetime

from django.db import models

from .compat import AUTH_USER_MODEL
from .managers import BasisModelManager


class BasisModel(models.Model):
    deleted = models.BooleanField(default=False, editable=False)

    created_at = models.DateTimeField(default=datetime.now, editable=False, auto_now_add=True)
    created_by = models.ForeignKey(AUTH_USER_MODEL, null=True, default=None, editable=False,
                                   related_name="%(class)s_created")

    updated_at = models.DateTimeField(default=datetime.now, editable=False, auto_now=True)
    updated_by = models.ForeignKey(AUTH_USER_MODEL, null=True, default=None, editable=False,
                                   related_name="%(class)s_updated")

    objects = BasisModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        if 'current_user' in kwargs:
            current_user = kwargs.pop("current_user")

            if not self.id:
                self.created_by = current_user

            self.updated_by = current_user

        super(BasisModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def restore(self, *args, **kwargs):
        self.deleted = False
        self.save()

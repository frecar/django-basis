from datetime import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

from .compat import AUTH_USER_MODEL
from .managers import BasisModelManager


def _now():
    if settings.USE_TZ:
        return timezone.now()
    return datetime.now()


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(default=_now, editable=False)
    updated_at = models.DateTimeField(default=_now, editable=False)

    def save(self, *args, **kwargs):
        self.updated_at = _now()
        super(TimeStampModel, self).save(*args, **kwargs)


class BasisModel(TimeStampModel):
    deleted = models.BooleanField(default=False, editable=False)

    created_by = models.ForeignKey(AUTH_USER_MODEL, null=True, default=None, editable=False,
                                   related_name="%(class)s_created")
    updated_by = models.ForeignKey(AUTH_USER_MODEL, null=True, default=None, editable=False,
                                   related_name="%(class)s_updated")

    objects = BasisModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__set_user(kwargs)
        super(BasisModel, self).save(*args, **kwargs)

    def __set_user(self, kwargs):
        if 'current_user' in kwargs:
            current_user = kwargs.pop("current_user")

            if not self.id:
                self.created_by = current_user

            self.updated_by = current_user

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save(*args, **kwargs)

    def restore(self, *args, **kwargs):
        self.deleted = False
        self.save(*args, **kwargs)

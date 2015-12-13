from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

from .managers import BasisModelManager, PersistentModelManager


def _now():
    if settings.USE_TZ:
        return timezone.now()
    return datetime.now()


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(default=_now, editable=False)
    updated_at = models.DateTimeField(default=_now, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = _now()
        super(TimeStampModel, self).save(*args, **kwargs)


class PersistentModel(models.Model):
    deleted = models.BooleanField(default=False, editable=False)

    objects = PersistentModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, force=False):
        if force:
            super(PersistentModel, self).delete(using)
        else:
            self.deleted = True
            self.save()

    def restore(self, *args, **kwargs):
        self.deleted = False
        self.save(*args, **kwargs)


class BasisModel(TimeStampModel, PersistentModel):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   default=None, editable=False,
                                   related_name="%(class)s_created")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   default=None, editable=False,
                                   related_name="%(class)s_updated")

    objects = BasisModelManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        try:
            kwargs['current_user'] = self.current_user
        except AttributeError:
            pass
        self.__set_user(kwargs)
        super(BasisModel, self).save(*args, **kwargs)

    def __set_user(self, kwargs):
        if 'current_user' in kwargs:
            current_user = kwargs.pop("current_user")

            if not self.id:
                self.created_by = current_user

            self.updated_by = current_user

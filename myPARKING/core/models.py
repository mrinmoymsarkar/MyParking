"""
Core model to put common items into databases
"""
from datetime import datetime

from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    created and modified fields.
    """
    created = models.DateTimeField('created')
    modified = models.DateTimeField('modified')

    def save(self, *args, **kwargs):
        if not self._check_id_field:
            self.created = datetime.today()
        self.modified = datetime.today()
        return super(TimeStampedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

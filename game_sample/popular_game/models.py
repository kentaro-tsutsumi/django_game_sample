import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

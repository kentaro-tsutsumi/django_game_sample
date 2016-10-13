import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Player(Base):
    name = models.CharField(max_length=10, db_index=True)
    level = models.IntegerField(blank=False, default=1)
    exp = models.BigIntegerField(default=0)
    LEVEL_EXPS = [0, 100, 200, 300, 400, 500]

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        setattr(self, 'initial_exp', self.exp)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.initial_exp != self.exp:
            for i, level_exp in enumerate(self.LEVEL_EXPS):
                if self.exp >= level_exp:
                    self.level = i + 1
                else:
                    break
        super(Player, self).save(*args, **kwargs)

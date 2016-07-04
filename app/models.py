from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField(null=True)
    cr_time = models.CharField(null=True, max_length=100)
    short_url = models.URLField(null=True)
    clicks = models.IntegerField(null=True, default=0)


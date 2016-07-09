from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField(null=True)
    cr_time = models.DateTimeField(null=True, auto_now_add=True)
    short_url = models.URLField(null=True, max_length=100, unique=True)
    clicks = models.IntegerField(null=True, default=0)


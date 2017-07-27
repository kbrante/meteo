# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Refresh(models.Model):
    datetime = models.DateTimeField()
    ip = models.CharField(max_length=20)
    url = models.CharField(max_length=500)

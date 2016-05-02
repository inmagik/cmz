from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    text = models.TextField()
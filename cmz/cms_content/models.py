from __future__ import unicode_literals

from django.db import models

#TODO: derive from base model defined in cms_core
class TextContent(models.Model):
    """
    """
    key = models.CharField(max_length=200, unique=True)
    content = models.TextField()



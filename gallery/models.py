from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class ImgModel(models.Model):
    img = models.ImageField(upload_to='upload')

    def __str__(self):
        return str(self.img)

from django.db import models

# Create your models here.


class LopHoc(models.Model):
    tenlop = models.CharField(default='', blank=True, max_length=255)
    sophong = models.IntegerField(default=0)

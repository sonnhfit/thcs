from django.db import models

# Create your models here.


class TenDanhMuc(models.Model):
    tendanhmuc = models.CharField(max_length=255, null=True, blank=True)
    mota = models.CharField(max_length=255, null=True, blank=True)
    kieudanhmuc = models.IntegerField(default=0)

from django.db import models
from lop.models import LopHoc
from users.models import *
# Create your models here.


class MonHoc(models.Model):
    tenmonhoc = models.CharField(max_length=255)
    sotiethoc = models.IntegerField(default=0)


class DiemSo(models.Model):
    monhoc = models.ForeignKey(MonHoc, on_delete=models.CASCADE)
    lop = models.ForeignKey(LopHoc, on_delete=models.CASCADE)
    hocsinh = models.ForeignKey(HocSinh, on_delete=models.CASCADE)
    giaovien = models.ForeignKey(GiaoVien, on_delete=models.CASCADE)
    d15p = models.FloatField(default=0)
    d45p = models.FloatField(default=0)
    giuaky = models.FloatField(default=0)
    cuoiky = models.FloatField(default=0)


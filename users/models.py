from django.db import models
from lop.models import LopHoc
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    hoten = models.CharField(default='', null=True, blank=True, max_length=255)
    ngaysinh = models.DateField()
    diachi = models.CharField(default='', null=True, blank=True, max_length=255)
    tongiao = models.CharField(default='', null=True, blank=True, max_length=255)
    dienthoai = models.CharField(default='', null=True, blank=True, max_length=255)
    quyen  = models.IntegerField(default=0)


class GiaoVien(User):
    trinhdo = models.CharField(default='', null=True, blank=True, max_length=255)


class HocSinh(User):
    lop = models.ForeignKey(LopHoc, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    hoten = models.CharField(default='', null=True, blank=True, max_length=255)
    ngaysinh = models.DateField(auto_now_add=True)
    diachi = models.CharField(default='', null=True, blank=True, max_length=255)
    tongiao = models.CharField(default='', null=True, blank=True, max_length=255)
    dienthoai = models.CharField(default='', null=True, blank=True, max_length=255)
    quyen = models.IntegerField(default=0)

    @property
    def is_hocsinh(self):
        if self.quyen == 1:
            return True
        else:
            return False

    @property
    def is_giaovien(self):
        if self.quyen == 2:
            return True
        else:
            return False

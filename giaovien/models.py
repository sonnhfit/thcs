from django.db import models
from danhmuc.models import *
from users.models import *
# Create your models here.


class GiaoVien(models.Model):
    TRINH_DO = (
        ('DH', 'Cử nhân'),
        ('THS', 'Thạc sĩ'),
        ('TS', 'Tiến sĩ'),
        ('GS', 'Giáo sư'),
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Tài khoản')
    trinhdo = models.CharField(
        default='DH', choices=TRINH_DO, null=True, blank=True, max_length=255, verbose_name='Trình độ')

    def __str__(self):
        return '%s - %s'%(self.trinhdo, self.user.hoten)

    class Meta:
        verbose_name_plural = "Giáo viên"


class LichGiangDay(models.Model):
    giaovien = models.ForeignKey(GiaoVien, default=models.CASCADE, on_delete=models.CASCADE, verbose_name='Giáo viên')
    thoigian = models.DateTimeField(verbose_name='Thời gian')
    monday = models.ForeignKey(MonHoc, on_delete=models.CASCADE, verbose_name='Môn dạy')

    def __str__(self):
        return 'Lịch giảng dạy của: %s'%self.giaovien.__str__()

    class Meta:
        verbose_name_plural = "Lịch giảng dạy"

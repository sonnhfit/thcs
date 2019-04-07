from django.db import models

# Create your models here.


class KyHoc(models.Model):
    ten_ky_hoc = models.CharField(default='', max_length=255, verbose_name='Tên kỳ học')

    class Meta:
        verbose_name_plural = "Kỳ học"


class KhoiHoc(models.Model):
    ten_khoi_hoc = models.CharField(default='', max_length=255, verbose_name='Tên khối học')

    def __str__(self):
        return self.ten_khoi_hoc

    class Meta:
        verbose_name_plural = "Khối học"


class LopHoc(models.Model):
    ten_lop_hoc = models.CharField(default='', max_length=255, verbose_name='Tên lớp học')
    khoi_hoc = models.ForeignKey(KhoiHoc, on_delete=models.CASCADE, verbose_name='Khối học')

    def __str__(self):
        return self.ten_lop_hoc

    class Meta:
        verbose_name_plural = "Lớp học"


class MonHoc(models.Model):
    ten_mon_hoc = models.CharField(default='', max_length=255, verbose_name='Tên môn học')
    so_tiet = models.IntegerField(default=0, verbose_name='Số tiết học')

    def __str__(self):
        return self.ten_mon_hoc

    class Meta:
        verbose_name_plural = "Môn học"



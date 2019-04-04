from django.db import models
from users.models import *
from monhoc.models import *
# Create your models here.


class LichGiangDay(models.Model):
    giaovien = models.ForeignKey(GiaoVien, on_delete=models.CASCADE)
    lop = models.ForeignKey(LopHoc, on_delete=models.CASCADE)
    tiet = models.IntegerField(default=0)
    thu = models.IntegerField(default=0)
    mon = models.ForeignKey(MonHoc, on_delete=models.CASCADE)


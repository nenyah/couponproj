from django.db import models

__all__ = ('Client', 'Verifier')

# Create your models here.
# 机构
from coupon.models import Base


class Client(Base):
    client = models.CharField(max_length=100, verbose_name="机构")

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.client


# 核销员
class Verifier(Base):
    verifier = models.CharField(max_length=100, verbose_name="核销员")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="机构")

    class Meta:
        verbose_name = '核销员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.verifier

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
__all__ = ('Client', 'Verifier')


# 基类
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        abstract = True


# 机构
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

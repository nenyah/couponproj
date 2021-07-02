from django.db import models

__all__ = ('User', 'Activity', 'Token', 'Coupon', 'CouponUse')


# Create your models here.
# 基类
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        abstract = True


# 用户实体类
class User(Base):
    user_uuid = models.CharField(max_length=64, verbose_name='uuid', unique=True)
    username = models.CharField(max_length=32, null=True, verbose_name='用户名')
    user_js_code = models.CharField(max_length=64, verbose_name='用户js_code')
    login_time = models.DateTimeField(auto_now=True, verbose_name='登录时间')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')

    class Meta:
        verbose_name = '微信用户'
        verbose_name_plural = verbose_name

    #     managed = False
    #     db_table = 'wechat_user'

    def __str__(self):
        return self.user_uuid


# 活动
class Activity(Base):
    activity = models.CharField(max_length=100, verbose_name="活动")

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.activity


# Token
class Token(Base):
    token = models.UUIDField(verbose_name='token')
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='关联用户')

    class Meta:
        verbose_name = 'token'
        verbose_name_plural = verbose_name


# 优惠券
class Coupon(Base):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name="活动")
    coupon_name = models.CharField(max_length=64, verbose_name='优惠券标题')
    coupon_type_choices = ((1, '满减优惠券'), (2, '通用优惠券'))
    coupon_type = models.IntegerField(choices=coupon_type_choices, verbose_name='优惠券类型')
    amount = models.CharField(max_length=32, verbose_name='等值金额')
    coupon_number = models.PositiveIntegerField(verbose_name='数量')
    min_amount = models.CharField(max_length=32, default=0, verbose_name='最低消费金额', help_text='满减劵时填写')
    receive_time = models.DateTimeField(verbose_name='优惠券开始发放时间')
    effective_time = models.DateTimeField(verbose_name='优惠券生效时间')
    invalid_time = models.DateTimeField(verbose_name='优惠券失效时间')

    def __str__(self):
        return '{}-{}'.format(self.coupon_name, self.get_coupon_type_display())

    class Meta:
        verbose_name = '优惠券'
        verbose_name_plural = verbose_name


# 优惠券使用
class CouponUse(Base):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='绑定用户')
    coupon = models.ForeignKey(to=Coupon, on_delete=models.CASCADE, verbose_name='优惠券')
    status_choices = ((1, '未使用'), (2, '已使用'), (3, '已过期'))
    status = models.IntegerField(choices=status_choices, verbose_name='用户优惠券状态')
    obtain_time = models.DateTimeField(verbose_name='领取时间')
    coupon_use_time = models.DateTimeField(null=True, verbose_name='使用时间')

    def __str__(self):
        return '{}-{}'.format(self.user, self.coupon)

    class Meta:
        verbose_name = '优惠券使用记录'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'coupon')  # 联合约束，用户与优惠券类型

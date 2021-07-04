from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'user')


@admin.register(models.WechatUser)
class WechatUserAdmin(admin.ModelAdmin):
    list_display = (
        "user_uuid",
        "username",
        "user_js_code",
        "login_time",
        "is_active",
    )


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity', 'create_by')
    exclude = ('create_by',)

    def save_model(self, request, obj, form, change):
        obj.create_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'coupon_name', 'activity',
        'coupon_type', 'amount',
        'coupon_number', 'min_amount',
        'receive_time', 'effective_time',
        'invalid_time')
    exclude = ('create_by',)

    def save_model(self, request, obj, form, change):
        obj.create_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.CouponUse)
class CouponUseAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "coupon",
        "status",
        "obtain_time",
        "coupon_use_time",
        "verifier",
    )

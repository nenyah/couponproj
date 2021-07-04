from rest_framework import serializers
from .models import Activity, Coupon
from django.contrib.auth import get_user_model

User = get_user_model()


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ('id', 'create_by')


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
        read_only_fields = ('id', 'create_by')

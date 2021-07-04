from django.urls import path, include
from rest_framework import routers

from . import views
from .views import LoginView

router = routers.DefaultRouter()
router.register(r'activities', views.ActivityViewSet)
router.register(r'coupons', views.CouponViewSet)

urlpatterns = [
    # 登录
    path('login', LoginView.as_view()),
    path('', include((router.urls, 'coupon'))),
]

import uuid

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from utils import wx_auth, authentication
from .models import Activity, WechatUser, Token, Coupon
from .serializers import ActivitySerializer, CouponSerializer


# 登录
class LoginView(APIView):
    def post(self, request):
        req_data = request.data
        # 获取传递的code
        code = req_data.get('code', '')
        # 判断是否有code
        if not code:
            return Response({'error': '没有获取到code'})
        try:
            # 获取openid
            auth_code = wx_auth.auth_code2session(code)
            openid = auth_code.get('openid', '')
            # 判断是否是正确的openid
            if not openid:
                return Response({'error': '错误的code'})
            # 验证数据库是否存在该用户,判断其状态是否激活
            user_obj_false = WechatUser.objects.filter(user_uuid=openid, is_active=False).first()
            if user_obj_false:
                return Response({'error': '该用户已存在但未激活'})
            # 验证数据库是否存在该用户,不存在则创建
            user_obj = WechatUser.objects.filter(user_uuid=openid, is_active=True).first()
            token = uuid.uuid4()
            if not user_obj:
                # 创建用户，返回token
                user_obj_code = WechatUser.objects.create(user_js_code=code, user_uuid=openid)
                Token.objects.create(token=token, user=user_obj_code)
                return Response({'userID': user_obj_code.id, 'token': token})
            # 如果存在该用户，则更新token后返回
            try:
                Token.objects.filter(user=user_obj).update(token=token)
            except Exception as e:
                return Response({'error': '登录失败'})
            return Response({'userID': user_obj.id, 'token': token})
        except Exception as e:
            return Response({'error': '登录异常错误'})


class ActivityViewSet(ModelViewSet):
    authentication_classes = [authentication.LoginAuth]
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class CouponViewSet(ModelViewSet):
    authentication_classes = (authentication.LoginAuth,)
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.timezone import now
from coupon.models import Token

# 过期时间
EXPIRED_TIME = 15


# 登录认证
class LoginAuth(BaseAuthentication):
    def authenticate(self, request):
        # 获取token
        token = request.META.get('HTTP_AUTHORIZATION', '')
        # 判断是否携带token
        if not token:
            raise AuthenticationFailed({"code": 1020, "error": "没有携带token"})

        token_obj = Token.objects.filter(token=token).first()
        # 判断是否存该token
        if not token_obj:
            raise AuthenticationFailed({'error': 'token不正确'})
        # 获取token保存的时间，与当前时间
        token_time = token_obj.created
        now_time = now()
        # 判断用户是否登录超时
        if (now_time - token_time).days > EXPIRED_TIME:
            raise AuthenticationFailed({'error': '登录过期，请重新登录'})
        return token_obj, token

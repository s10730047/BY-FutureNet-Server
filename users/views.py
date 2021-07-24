from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from users.models import Users
from users.serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST', 'DELETE']) 

def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            users = users.filter(title__icontains=title)
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_serializer = UsersSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):

    renderer_classes = [JSONRenderer]   # json渲染器
    authentication_classes = []         # 此方法不验证JWT
    permission_classes = []             # 此方法不设权限
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        username = request.data.get("username", 0)
        password = request.data.get("password", 0)
        if username and password:
            # 校验注册，名字不可重复
            user = Users.objects.filter(username=username).first()
            if user:
                content = {'msg': '用户已存在'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:
                # 注册成功，创建用户
                Users.objects.create(
                    username=username,
                    password=password
                )
                content = {'msg': '注册成功'}
                return Response(content, status=status.HTTP_201_CREATED)
        content = {'msg': '账号或密码不能为空'}
        return Response(content, status=status.HTTP_403_FORBIDDEN)



class LoginView(APIView):
    renderer_classes = [JSONRenderer]   # json渲染器
    authentication_classes = []         # 此方法不验证JWT
    permission_classes = []             # 此方法不设权限
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        username = request.data.get("username", 0)
        password = request.data.get("password", 0)
        if not username or not password:
            content = {'msg': '输入的账号或密码有误'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = Users.objects.filter(username=username).first()
            if not user:
                content = {'msg': '输入的账号或密码有误'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:

                # 生成token的业务逻辑 start
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)

                token_with_JWT = "JWT " + token     # 为token添加JWT头后保存到数据库
                user.token = token_with_JWT
                user.save()
                # 生成token的业务逻辑 end

                content = {'登入成功~Authorization': token_with_JWT}
                return Response(content, status=status.HTTP_200_OK)

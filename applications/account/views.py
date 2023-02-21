from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from applications.account.serializers import LoginSerializer ,RegisterSerializer ,ChangePasswordSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

# Create your views here.

User = get_user_model()

class RegisterAPIView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('ВЫ зарегались.Осталось активировать ваш аккаунт', status=201)


class LogoutAPIView(APIView):
    permission_classes =[IsAuthenticated]
    def post(self,request):
        try:
            user = request.user
            Token.objects.get(user=user).delete()
            return Response('Вы успешно разлогинились',status=200)
        except:
            return Response(status=403)

class LoginAPIVeiw(ObtainAuthToken):
    serializer_class = LoginSerializer

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code =''
            user.save()
            return Response('Успешно', status= 200)
        except User.DoesNotExist:
            return Response('Что-то пошло не так',status=400)


from django.contrib.auth.hashers import check_password

class ChangePasswordView(generics.UpdateAPIView):
    """
    API endpoint для смены пароля пользователя
    """
    model = User
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # проверяем старый пароль
            old_password = serializer.data.get("old_password")
            if check_password(old_password, self.object.password):
                # сохраняем новый пароль
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'message': 'Пароль успешно изменен'
                }
                return Response(response, status=status.HTTP_200_OK)

            else:
                response = {
                    'status': 'failed',
                    'message': 'Старый пароль неверный'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
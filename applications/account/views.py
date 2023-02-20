from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from applications.account.serializers import LoginSerializer ,RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response


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
    




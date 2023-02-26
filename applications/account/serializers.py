from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from applications.account.send_email import send_activateion_code


User =get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required = True,min_length=2,write_only = True)

    class Meta:
        model = User
        fields = ('email','password','password2')
    
    def validate_email(self, email):
        print('Okay.Email sending')
        return email
    

    def validate(self,attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError('Неправильный пароль!')
        
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activateion_code(user.email, user.activation_code)
        return user

    


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)


    def validate_email(self, email ):
        if User.objects.filter(email = email).exists():
            return email
        raise serializers.ValidationError('Пользователь не найден')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user =authenticate(username = email, password = password)
        if not User:
            raise serializers.ValidationError('Неверный пароль')
        attrs['user'] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("Пароль должен содержать хотя бы 2 символа")

        return value

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Старый пароль неверный")

        return value


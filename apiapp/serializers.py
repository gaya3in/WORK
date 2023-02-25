from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Work, Artist
from django.core.exceptions import ObjectDoesNotExist

class WorkSerializer(serializers.ModelSerializer):

    artist = serializers.SerializerMethodField('get_artist')

    class Meta:
        model = Work
        fields = "__all__"

    def get_artist(self,objWork):
        global artist

        try:
            artist = Artist.objects.get(work=objWork).name
            return artist
        except ObjectDoesNotExist:
            return ""


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:        
                user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
                if not user or not user.is_active:
                    # If we don't have a regular user, raise a ValidationError
                    msg = 'Access denied: wrong username or password.'
                    raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='Invalid input')
        attrs['user'] = user
        return attrs
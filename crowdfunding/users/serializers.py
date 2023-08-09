from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'
        extra_kwargs = {'password': {'write_only': True}}  # we don't want our serializer to show our password to anyone.  we tell the serializer that we have an extra "keyword argument" for thepassword field. This is an extra piece of info about how this field should be serialized.Specifically, it is write_only. The serializer will send it to the model when a new user is created, but will neverbounce it back to the user.

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
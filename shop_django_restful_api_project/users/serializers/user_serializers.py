from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    first_name          = serializers.CharField(allow_blank=False, write_only=True)
    last_name           = serializers.CharField(allow_blank=False, write_only=True)
    confirm_password    = serializers.CharField(allow_blank=False, write_only=False)

    class Meta:
        model = get_user_model()
        fields = ("phone_number", "first_name", "last_name", "password", "confirm_password")

    def create(self, validated_data):
        confirm_password = validated_data.pop("confirm_password")
        return get_user_model().objects.create_user(**validated_data)

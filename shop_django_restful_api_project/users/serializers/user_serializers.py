from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class UserSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(allow_blank=False, write_only=True)
    last_name = serializers.CharField(allow_blank=False, write_only=True)
    confirm_password = serializers.CharField(allow_blank=False, write_only=False)

    class Meta:
        model = get_user_model()
        fields = ("phone_number", "first_name", "last_name", "password", "confirm_password")

    def validate(self, attrs):
        if not self.is_equal_password_and_repeated(attrs.get("password"), attrs.pop("confirm_password")):
            raise serializers.ValidationError({"password": _("password and confirm_password is not equal")})
        return attrs

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def validate_password(self, password):
        if password.startswith("1234"):
            raise serializers.ValidationError(_("Password can't starts with 1234"))
        return password

    def is_equal_password_and_repeated(self, password=None, repeat_password=None):
        return True if password and repeat_password and password == repeat_password else False

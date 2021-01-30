from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from users.serializers.user_serializers import UserSerializers


class SignUpView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data

        serializer = UserSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            res_data = {
                "phone_number": data.get("phone_number"),
                "first_name": data.get("first_name"),
                "last_name": data.get("last_name"),
            }
            return Response(data=res_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=404)
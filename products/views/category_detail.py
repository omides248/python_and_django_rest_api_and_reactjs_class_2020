from django.http import Http404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models.category import Category
from products.serializers.category_serializer import CategorySerializer, CategoryUpdateSerializer


class CategoryDetailView(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category_obj = self.get_object(pk)
        serializer = CategorySerializer(instance=category_obj, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        category_obj = self.get_object(pk)
        serializer = CategoryUpdateSerializer(instance=category_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, 400)

    def delete(self, request, pk):
        category_obj = self.get_object(pk)
        category_obj.delete()
        return Response()

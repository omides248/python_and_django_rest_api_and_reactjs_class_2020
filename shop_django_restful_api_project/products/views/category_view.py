from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, generics, mixins, filters
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models.category import Category
from products.models.product import Product
from products.serializers.category_serializer import CategorySerializer, CategoryUpdateSerializer
from products.serializers.product_serializer import ProductSerializer
from products.views.product_view import LargeResultsSetPagination


class CategoryView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        serializer = CategorySerializer(instance=Category.objects.all(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)


class CategoryView2(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404

    def list(self, request, *args, **kwargs):
        serializer = CategorySerializer(instance=Category.objects.all(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)

    def retrieve(self, request, pk):
        category_obj = self.get_object(pk)
        serializer = CategorySerializer(instance=category_obj, context={"request": request})
        return Response(serializer.data)

    def update(self, request, pk):
        category_obj = self.get_object(pk)
        serializer = CategoryUpdateSerializer(instance=category_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 400)

    def destroy(self, request, pk):
        category_obj = self.get_object(pk)
        category_obj.delete()
        return Response()


class CategoryView3(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    pagination_class = LargeResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'active']
    search_fields = ['name', 'active']

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def patch(self, request, pk, *args, **kwargs):
        return self.partial_update(request, pk, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.delete(request, pk, *args, **kwargs)

    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, 201)
    #     return Response(serializer.errors, 400)


class CategoryView4(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    pagination_class = LargeResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'active']
    search_fields = ['name', 'active']

    @action(detail=True, methods=["GET"])
    def products(self, request, pk=None):
        self.filterset_fields = ['name']
        self.search_fields = ['name']
        queryset = self.filter_queryset(Product.objects.filter(category=pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryView5(generics.ListCreateAPIView):
    pass

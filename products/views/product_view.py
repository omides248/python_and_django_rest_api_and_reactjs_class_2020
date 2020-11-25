from rest_framework import generics, viewsets, mixins, serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated

from products.models.product import Product
from products.serializers.product_serializer import ProductSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProductView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = LargeResultsSetPagination


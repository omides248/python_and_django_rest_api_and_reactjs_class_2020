from django.urls import re_path
from rest_framework.routers import DefaultRouter

from products.views.category_detail import CategoryDetailView
from products.views.category_view import CategoryView, CategoryView2, CategoryView3, CategoryView4
from products.views.product_view import ProductView

router = DefaultRouter()
# You can only use `auto create urls` in `viewsets`
router.register("products", ProductView, basename="product-url")  # This view is `viewsets (ModelViewSet)`
router.register("categories2", CategoryView2, basename="category_2")  # This view is `viewsets (ViewSet)`
router.register("categories4", CategoryView4, basename="category_4")  # This view is `viewsets (GenericViewSet)`

urlpatterns = [
    re_path(r"categories/?$", CategoryView.as_view()),  # This view is `APIView`
    re_path(r"categories/(?P<pk>\d+)/?$", CategoryDetailView.as_view()),  # This view is `APIView`

    # re_path(r"categories2/$", CategoryView2.as_view({"get": "list", "post": "create"})),  # This view is `viewsets (ViewSet)`

    re_path(r"categories3/?$", CategoryView3.as_view()),  # This view is `generics (GenericAPIView)`
    re_path(r"categories3/(?P<pk>\d+)/?$", CategoryView3.as_view()),  # This view is `generics (GenericAPIView)`

]

urlpatterns += router.urls

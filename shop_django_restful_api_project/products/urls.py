from django.urls import re_path
from rest_framework.routers import DefaultRouter

from products.views.category_detail import CategoryDetailView
from products.views.category_view import CategoryView
from products.views.product_view import ProductView

router = DefaultRouter()
router.register("products", ProductView, basename="product-url")

urlpatterns = [
    re_path(r"categories/?$", CategoryView.as_view()),
    re_path(r"categories/(?P<pk>\d+)/?$", CategoryDetailView.as_view())
]

urlpatterns += router.urls

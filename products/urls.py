from django.urls import re_path

from products.views.category_detail import CategoryDetailView
from products.views.category_view import CategoryView

urlpatterns = [
    re_path(r"categories/?$", CategoryView.as_view()),
    re_path(r"categories/(?P<pk>\d+)/?$", CategoryDetailView.as_view())
]

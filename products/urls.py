from django.urls import path

from products.views import CategoryListAPIView, ProductListAPIView, ProductRetrieveAPIView

app_name = 'products'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', ProductListAPIView.as_view()),
    path('search/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view()),
]

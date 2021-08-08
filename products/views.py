from rest_framework.generics import ListAPIView, RetrieveAPIView

from products.models import CategoryModel, ProductModel
from products.serializers import CategoryModelSerializer, ProductModelSerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        q = self.request.GET.get('q')

        if pk:
            return ProductModel.objects.filter(category_id=pk)
        elif q:
            return ProductModel.objects.filter(title__icontains=q)
        else:
            return ProductModel.objects.none()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()

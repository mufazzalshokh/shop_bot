from rest_framework import serializers

from products.models import CategoryModel, ProductModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()

    class Meta:
        model = ProductModel
        fields = '__all__'

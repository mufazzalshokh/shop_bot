from django.db import models
from django.db.models import PROTECT


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(CategoryModel, on_delete=PROTECT, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

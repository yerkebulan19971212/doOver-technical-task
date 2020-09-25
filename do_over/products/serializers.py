from rest_framework import serializers
from .models import Products, HistoryOfProduct
from ..extra.serializers import ListCategoriesSerializer, ImageSerializer


class ListProductsSerializer(serializers.ModelSerializer):
    category = ListCategoriesSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = ("name", "category", "description", "images")


class HistoryOfUserProductSerializer(serializers.ModelSerializer):
    product = ListProductsSerializer(read_only=True)
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = HistoryOfProduct
        fields = ('product', 'status')

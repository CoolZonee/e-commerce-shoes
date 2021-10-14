from django.db.models import fields
from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductRetrieveSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['upc', 'name', 'quantity', 'gender', 'price',
                  'cost', 'desc', 'brand', 'supplier', 'type', 'date']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

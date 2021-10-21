from django.contrib import admin

from products.models import Brand, Gender, Product, ProductDetails, Supplier, Type

admin.site.register(Type)
admin.site.register(Supplier)
admin.site.register(Gender)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductDetails)

from django.db import models
from django.db.models.deletion import CASCADE, PROTECT


class Type(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    upc = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    gender = models.ManyToManyField(Gender)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    desc = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.upc + ' - ' + self.name

from django.db import models


# Create your models here.

# Category model
class Category(models.Model):
    cat_name = models.CharField(max_length=45)

    def __str__(self):
        return self.cat_name

# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    address = models.CharField(max_length=45)

# Product model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_name = models.CharField(max_length=45)
    unit_price = models.IntegerField()
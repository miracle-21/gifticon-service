from django.db import models


class User(models.Model):
    name   = models.CharField(max_length = 200)

    class Meta():
        db_table = 'users'


class Product(models.Model):
    name   = models.CharField(max_length = 200)
    demand = models.IntegerField()
    supply = models.IntegerField()

    class Meta():
        db_table = 'products'


class Waiting(models.Model):
    user    = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    waiting  = models.IntegerField()

    class Meta():
        db_table = 'waitings'
        
from django.db import models


class User(models.Model):

    class Meta():
        db_table = 'users'


class Product(models.Model):
    name   = models.CharField(max_length = 200)
    demand = models.IntegerField()
    supply = models.IntegerField()

    class Meta():
        db_table = 'products'


class UserWaiting(models.Model):
    user          = models.ForeignKey('User', on_delete = models.CASCADE)
    product       = models.ForeignKey('Product', on_delete = models.CASCADE)
    wating_number = models.IntegerField()

    class Meta():
        db_table = 'user_waitings'
        
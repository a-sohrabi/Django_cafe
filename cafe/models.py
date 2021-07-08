from django.db import models


# Create your models here.
class MenuItems(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.CharField(max_length=20)
    discount = models.IntegerField()
    serving_time_period = models.TimeField()
    estimated_cooking_time = models.TimeField()


class Table(models.Model):
    table_number = models.IntegerField()
    cafe_space_position = models.IntegerField()


class Orders(models.Model):
    number = models.IntegerField()
    status = models.CharField(max_length=20)
    menu_item_id = models.ForeignKey(MenuItems, on_delete=models.CASCADE, related_name='Receipt_User_id')
    time_stamp = models.DateTimeField()
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='Receipts_Orders_id')


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    birth_day = models.DateField()
    password_to_login = models.CharField(max_length=20)


class Receipts(models.Model):
    timestamp = models.DateTimeField()
    final_price = models.IntegerField()
    total_price = models.IntegerField()
    orders_id = models.ForeignKey(Orders, on_delete=models.CASCADE)





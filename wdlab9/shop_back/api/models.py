from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    desc = models.TextField(max_length=200)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def to_json(self):
        return {
            'name': self.name,
            'price': self.price,
            'desc': self.desc,
            'count': self.count,
            'is_active': self.is_active
        }


class Category(models.Model):
    name = models.CharField(max_length=100)

    def to_json(self):
        return {
            'name': self.name
        }

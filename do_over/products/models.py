from django.db import models
from ..extra.models import Category, Image, StatusProduct
from ..users.models import User


class Products(models.Model):
    name = models.CharField(max_length=220)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    description = models.TextField()
    images = models.ManyToManyField(Image)
    published = models.BooleanField(default=False)


class HistoryOfProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusProduct, on_delete=models.CASCADE)

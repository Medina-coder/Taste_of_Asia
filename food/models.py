from django.db import models

from category.models import Category
from user.serializers import User


class Foods(models.Model):
    title = models.TextField(verbose_name="title")
    price = models.CharField(max_length=50, verbose_name="price")

    class Meta:
        verbose_name = "Food"


class Food(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return f'{self.owner}--->{self.title}'


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField()

    class Meta:
        unique_together = ['owner', 'food']


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='images')


class Favorites(models.Model):
    owner = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='favorites')
    favorites = models.BooleanField()

    class Meta:
        unique_together = ['owner', 'food']




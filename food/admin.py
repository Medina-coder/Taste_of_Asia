from django.contrib import admin

from food.models import Food, Like, Favorites, Foods
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(Food)
admin.site.register(Like)
admin.site.register(Favorites)
admin.site.register(Foods)

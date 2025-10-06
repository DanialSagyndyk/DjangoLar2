#Django Modules
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    is_ative=models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Option(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='Menu_items')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='Menu_categories')
    options = models.ManyToManyField(Option, blank=True, related_name='Menu_options')
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.name

class Menu_options(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    additional_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.menu_item.name} - {self.option.name}"


class Menu_categories(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.menu_item.name} - {self.category.name}"
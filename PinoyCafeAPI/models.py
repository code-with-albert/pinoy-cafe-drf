from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length = 255, db_index = True)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length = 255, db_index=True)
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    featured = models.BooleanField(db_index = True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,db_index=True)
    menuitem = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1, validators = [MinValueValidator(1),MaxValueValidator(100)])
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return self.user
    
    class Meta:
        unique_together = ('menuitem','user')

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,db_index=True)
    menuitem = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1, validators = [MinValueValidator(1),MaxValueValidator(100)])
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return self.user
    
    class Meta:
        unique_together = ('menuitem','user')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, db_index=True)
    delivery_crew = models.ForeignKey(User, on_delete = models.SET_NULL,related_name='delivery_crew',null=True)
    status = models.BooleanField(default = 0, db_index=True)
    total_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    date = models.DateField(db_index = True)

    def __str__(self):
        return self.user + " : " + self.status + "  Date: " + self.date

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, db_index=True)
    menuitem = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1, validators = [MinValueValidator(1),MaxValueValidator(100)])
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return self.order
    

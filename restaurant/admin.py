from django.contrib import admin

# Register your models here.
from restaurant.models import *

class FoodItemInline(admin.StackedInline):
    model = FoodItem
    extra = 2

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name','address']
    inlines = [FoodItemInline]

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name']

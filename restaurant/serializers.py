from rest_framework import serializers
from .models import Restaurant,FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id','name','created_on','updated_on')
        read_only_field = ('id',)

class RestaurantSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True, source='fooditem_set') #Restaurant.fooditem_set.all()
    class Meta:
        model = Restaurant
        fields = ('id','name','address','phone_number','food_items','created_on','updated_on')
        #Read-only fields are included in the API output, but should not be included in the input during create or update operations
        read_only_field = ('id',)

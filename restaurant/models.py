from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    address = models.CharField(max_length=200)
    phone_number= models.CharField(max_length=20)

    created_on = models.DateTimeField(auto_now_add=True,editable=False)#when i created an object
    updated_on = models.DateTimeField(auto_now=True,editable=False)#when i update an object1

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=150, db_index= True)
    restaurant = models.ForeignKey('restaurant.Restaurant',on_delete=models.CASCADE)
    created_on = models.DateTimeField( auto_now_add=True, editable=False )  # when i created an object
    updated_on = models.DateTimeField( auto_now=True, editable=False )  # when i update an object1

    def __str__(self):
        return self.name

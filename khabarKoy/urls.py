from django.contrib import admin
from django.urls import path,include
from restaurant.views import *
from rest_framework_nested.routers import SimpleRouter,NestedSimpleRouter
from rest_framework.authtoken.views import obtain_auth_token

api_router = SimpleRouter(trailing_slash=False)
api_router.register('restaurants/',RestaurantViewSet, base_name='restaurant')
#apirouter = parent router
restaurant_router = NestedSimpleRouter(api_router,'restaurants/',lookup='reataurant')
restaurant_router.register('food_items/',FoodItemViewSet,base_name='food_item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(api_router.urls)),
    path('api/v1/',include(restaurant_router.urls)),
    path('api/v1/token/',obtain_auth_token)
]

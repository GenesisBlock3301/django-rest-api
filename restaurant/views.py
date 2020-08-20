import json

from django.http import HttpRequest, HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

from .models import *


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all().order_by("-created_on")
    serializer_class = RestaurantSerializer
    pagination_class = PageNumberPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

# Create your views here.

class FoodItemViewSet(ModelViewSet):
    queryset = FoodItem.objects.all().order_by("-created_on")
    serializer_class = FoodItemSerializer
    pagination_class = PageNumberPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    # def list(self, request,):
    #     queryset = FoodItem.objects.filter()
    #     serializer = FoodItemSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = FoodItem.objects.filter()
    #     item = get_object_or_404(queryset, pk=pk)
    #     serializer = FoodItemSerializer(item)
    #     return Response(serializer.data)

@csrf_exempt
def restaurant_handler(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return list_restaurant(request)
    if request.method == "POST":
        return create_restaurant(request)


def list_restaurant(request: HttpRequest) -> HttpResponse:
    queryset = Restaurant.objects.all()\
        .order_by('-created_on')\
        .values('name','address','phone_number')
    return JsonResponse(list(queryset),safe=False)

def create_restaurant(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    obj = Restaurant(name=data['name'],address=data['address'],phone_number=data['phone_number'])
    obj.save()
    return JsonResponse({
        'id': obj.id,
        **data,

    } )
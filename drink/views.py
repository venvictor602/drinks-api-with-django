from django.shortcuts import render
from .models import Drink
from django.http import JsonResponse
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular .utils import extend_schema

@extend_schema(responses=DrinkSerializer)
@api_view(["GET", "POST"])
def drinklist(request):
    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many = True)
        return Response({"drinks": serializer.data}, status=status.HTTP_302_FOUND)
    
    if request.method =="POST":
        serializer = DrinkSerializer(data = request.data) #this is used to tell the api that the data to be saved is the  data that was passed in the request to be saved in the model
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)



@extend_schema(responses=DrinkSerializer)
@api_view(["GET", "PUT", "DELETE"])     
def drink_detail(request, id):
    try:
        drink = Drink.objects.get(pk = id)
    except Drink.DoesNotExist:
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    
    if request.method =="GET":
        serializer = DrinkSerializer(drink)
        return Response({"Drink": serializer.data}, )
    
    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data) # the put is used to update which will apdate the drink model that has already been in the try block using the primary ir will update the model with the data sent in the request 
        if serializer.is_valid():
            serializer.save()        
            return Response({"Drink": serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED )


    elif request.method == "DELETE":
        drink.delete()
        return Response(status= status.HTTP_200_OK)


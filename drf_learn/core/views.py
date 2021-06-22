from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
# Create your views here.



@api_view(['GET','POST'])
def test(request):
    if request.method == "POST":
        query = request.data['query']
        number = request.data['number']
        apiKey = request.data['apiKey']
        cuisine = request.data['cuisine']
        fillIngredients = request.data['fillIngredients']
        diet = request.data['diet']
        r = requests.get('https://api.spoonacular.com/recipes/complexSearch?query='+query+'&number='+number+'&apiKey='+apiKey+'&cuisine='+cuisine+'&fillIngredients='+fillIngredients+'&diet='+diet)
        requested_data = r.json()
        results = requested_data['results']
        return Response(results[0]['missedIngredients'])
    else:
        return Response({"message": "Get METHOD"})
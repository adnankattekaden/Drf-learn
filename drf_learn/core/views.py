from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
from . models import MissedIngredients
from . serializers import MissedIngredientsSerializer
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
        for result in results[0]['missedIngredients']:
            MissedIngredients.objects.create(ids=result['id'],amount=result['amount'],unit=result['unit'],name=result['name'],image=result['image'])
        return Response(results[0]['missedIngredients'])
    else:
        missed_incrediants_data = MissedIngredients.objects.all()
        missed_incredients = MissedIngredientsSerializer(missed_incrediants_data,many=True)
        return Response(missed_incredients.data)
from rest_framework import serializers
from . models import MissedIngredients

class MissedIngredientsSerializer(serializers.ModelSerializer):
     class Meta:
        model = MissedIngredients
        fields = ['ids', 'amount', 'unit', 'name']

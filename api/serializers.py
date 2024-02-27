from rest_framework import serializers
from .models import *

class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItem
        fields = '__all__'
    
class CreatedStockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItem
        fields = ('name', 'description', 'location')
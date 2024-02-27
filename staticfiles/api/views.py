from django.http import JsonResponse
from django.shortcuts import render
from .models import * 
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.response import Response


"""
def get_stock(request):
    try:
        stock_i = StockItem.objects.all()
        stock = [{'id': item.id, 
                  'name': item.name, 
                  'description': item.description, 
                  'location': item.location} for item in stock_i]
        return JsonResponse(stock, safe=False)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
"""    

class StockItemViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer
    create_serializer_class = CreatedStockItemSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.create_serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            
            instance = self.queryset.get(pk=instance.id)
            print(instance.id)
            response_data = {
                'id': instance.id,
                'message': 'Object created successfully',
            }

            return Response(response_data, status=201)
            #return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        stock_item = self.queryset.get(pk=pk)
        print(stock_item)
        stock_item.delete()
        return Response(status=204)
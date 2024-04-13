from django.http import JsonResponse
from django.shortcuts import render
from .models import * 
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.response import Response
import json
from .mqtt_io import *

class StockItemViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer
    create_serializer_class = CreatedStockItemSerializer


    def list(self, request):
        queryset = StockItem.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.create_serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            data = request.data
            inbound_dock = 0
            message = json.dumps({
                "A": inbound_dock,
                "B": data['location']
            })
            if 'IOT_CONNECTION_STRING' in os.environ:
                send_mqtt_request(message)

            instance = self.queryset.get(pk=instance.id)
            response_data = {
                'id': instance.id,
                'message': 'Object created successfully',
            }

            return Response(response_data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        outbound_dock = 10
        stock_item = self.queryset.get(pk=pk)
        message = json.dumps({
            "A": stock_item.location,
            "B": outbound_dock    
        })
        if 'IOT_CONNECTION_STRING' in os.environ:
            send_mqtt_request(message)
        stock_item.delete()
        return Response(status=204)
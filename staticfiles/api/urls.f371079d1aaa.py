from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stock', StockItemViewset, basename='stockItem')
urlpatterns = router.urls

#urlpatterns = [
#    path('api/stock', views.get_stock),
#]

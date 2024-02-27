from django.db import models

class StockItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    location = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
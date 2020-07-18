from django.contrib import admin
from .models import Item, Project, StockLocation, StockItem

# Register your models here.

admin.site.register(StockLocation)
admin.site.register(Item)
admin.site.register(Project)
admin.site.register(StockItem)
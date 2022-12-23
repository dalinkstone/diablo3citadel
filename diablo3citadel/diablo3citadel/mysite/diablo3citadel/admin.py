from django.contrib import admin

# Register your models here.
from .models import ItemTypeIndex

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['id']}),
        ('Item Name',   {'fields': ['name']}),
        ('Item Path',   {'fields': ['path']}),
    ]


admin.site.register(ItemTypeIndex, ItemAdmin)
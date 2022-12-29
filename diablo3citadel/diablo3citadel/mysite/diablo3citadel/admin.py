from django.contrib import admin

# Register your models here.
from .models import ItemTypeIndex, ItemType

class ItemTypeIndexAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['id']}),
        ('Item Name',   {'fields': ['name']}),
        ('Item Path',   {'fields': ['path']}),
    ]
admin.site.register(ItemTypeIndex, ItemTypeIndexAdmin)

class ItemTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['id']}),
        ('Item Slug',       {'fields': ['slug']}),
        ('Item Name',       {'fields': ['name']}),
        ('Item Icon',       {'fields': ['icon']}),
        ('Item Path',       {'fields': ['path']}),
    ]
admin.site.register(ItemType, ItemTypeAdmin)
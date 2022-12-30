from django.contrib import admin

# Register your models here.
from .models import ItemTypeIndex, ItemType, Item

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

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                                  {'fields': ['id']}),
        ('Item Slug',                           {'fields': ['slug']}),
        ('Item Name',                           {'fields': ['name']}),
        ('Item Icon',                           {'fields': ['icon']}),
        ('Item Tooltip Params',                 {'fields': ['tooltipParams']}),
        ('Item Required Level',                 {'fields': ['requiredLevel']}),
        ('Item Stack Size Max',                 {'fields': ['stackSizeMax']}),
        ('Item Account Bound',                  {'fields': ['accountBound']}),
        ('Item Flavor Text',                    {'fields': ['flavorText']}),
        ('Item Flavor Text Html',               {'fields': ['flavorTextHtml']}),
        ('Item Type Name',                      {'fields': ['typeName']}),
        ('Item Type',                           {'fields': ['type']}),
        ('Item Damage',                         {'fields': ['damage']}),
        ('Item DPS',                            {'fields': ['dps']}),
        ('Item Damage Html',                    {'fields': ['damageHtml']}),
        ('Item Color',                          {'fields': ['color']}),
        ('Item Is Season Required To Drop',     {'fields': ['isSeasonRequiredToDrop']}),
        ('Item Season Required To Drop',        {'fields': ['seasonRequiredToDrop']}),
        ('Item Slots',                          {'fields': ['slots']}),
        ('Item Attributes',                     {'fields': ['attributes']}),
        ('Item Random Affixes',                 {'fields': ['randomAffixes']}),
        ('Item Set Items',                      {'fields': ['setItems']}),
    ]
admin.site.register(Item, ItemAdmin)

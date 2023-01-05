from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.template import loader
from .models import ItemTypeIndex, Item

# Create your views here.

def index(request):
    top_10_records = ItemTypeIndex.objects.order_by('-id')[:-10]
    top_10_items = Item.objects.order_by('-id')[:-10]
    context = {
        'top_10_records': top_10_records,
        'top_10_items': top_10_items,
    }
    return render(request, 'diablo3citadel/index.html', context)

def detail(request, itemtypeindex_id):
    record = get_object_or_404(ItemTypeIndex, pk=itemtypeindex_id)
    return render(request, 'diablo3citadel/detail.html', {'record': record})

def itemDetail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'diablo3citadel/detail.html', {'item': item})

def results(request, id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % id)\
        
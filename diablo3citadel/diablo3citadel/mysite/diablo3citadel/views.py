from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.template import loader
from .models import ItemTypeIndex

# Create your views here.

def index(request):
    top_5_records = ItemTypeIndex.objects.order_by('-id')[:5]
    context = {
        'top_5_records': top_5_records,
    }
    return render(request, 'diablo3citadel/index.html', context)

def detail(request, itemtypeindex_id):
    record = get_object_or_404(ItemTypeIndex, pk=itemtypeindex_id)
    return render(request, 'diablo3citadel/detail.html', {'record': record})

def results(request, id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % id)\
        
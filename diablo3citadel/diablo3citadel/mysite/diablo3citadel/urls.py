from django.urls import path
from . import views

urlpatterns = [
    # /itemtypeindex/
    path('', views.index, name='index'),
    # /itemtypeindex/HyperionSpear
    path('<str:itemtypeindex_id>/', views.detail, name='detail'),
    
    path('<str:item_id>/results', views.itemDetail, name='itemDetail'),
]
from django.urls import path
from . import views

urlpatterns = [
    # /itemtypeindex/
    path('', views.index, name='index'),
    # /itemtypeindex/HyperionSpear
    path('<str:itemtypeindex_id>/', views.detail, name='detail'),
    # /itemtypeindex/HyperionSpear/results
    path('<str:itemtypeindex_id>/results/', views.results, name='results'),
]
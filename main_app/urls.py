from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plants/', views.plants_index, name='plants'),
    path('plants/<int:plant_id>', views.plants_show, name='plants_show')
]
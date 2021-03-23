from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plants/', views.plants_index, name='plants'),
    path('plants/<int:plant_id>', views.plants_show, name='plants_show'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:pk>/add_gardening/', views.add_gardening, name = 'add_gardening')
]
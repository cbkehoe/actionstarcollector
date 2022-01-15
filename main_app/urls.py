from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stars/', views.stars_index, name='index'),
    path('stars/<int:star_id>/', views.stars_detail, name='detail'),
    path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
    path('stars/<int:pk>/update', views.StarUpdate.as_view(), name='stars_update'),
    path('stars/<int:pk>/delete', views.StarDelete.as_view(), name='stars_delete'),
    path('stars/<int:star_id>/add_weapon/', views.add_weapon, name='add_weapon'),
    path('stars/<int:star_id>/assoc_vehicle/<int:vehicle_id>/', views.assoc_vehicle, name='assoc_vehicle'),
    path('vehicles/', views.VehicleList.as_view(), name='vehicles_index'),
    path('vehicles/<int:pk>/', views.VehicleDetail.as_view(), name='vehicles_detail'),
    path('vehicles/create/', views.VehicleCreate.as_view(), name='vehicles_create'),
    path('vehicles/<int:pk>/update/', views.VehicleUpdate.as_view(), name='vehicles_update'),
    path('vehicles/<int:pk>/delete/', views.VehicleDelete.as_view(), name='vehicles_delete'),
]

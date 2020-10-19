from django.urls import path
from squirrel import views

urlpatterns = [
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/detail/<str:sid>', views.detail, name='detail'),
    path('sightings/add/', views.add, name='add'),
    path('map/', views.map, name='map'),
    path('sightings/stats/', views.stats,name='stats'),
]


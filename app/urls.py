from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.mainpage),
    path('sightings/', views.list),
    path('sightings/stats/', views.stats, name = 'stats'),
    path('sightings/add/', views.add, name = 'add'),
    path('sightings/<str:unique_squirrel_id>/', views.edit, name='edit'),
]

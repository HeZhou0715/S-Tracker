from django.urls import path

from . import views


urlpatterns = [
    path('', views.mainpage),
    path('sightings/', views.list),
    path('sightings/<str:unique_squirrel_id>/', views.edit, name='edit'),
]

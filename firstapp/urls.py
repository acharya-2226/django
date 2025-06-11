
from django.urls import path
from . import views
urlpatterns = [
    path('demo/', views.demo , name='demo'),
    path('countries/', views.countries, name='Country'),
    path('province/', views.province, name='Province'),
]

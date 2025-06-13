
from django.urls import path
from secondapp import views
urlpatterns = [
    path('contact-us/', views.contact_form, name='contact')


]

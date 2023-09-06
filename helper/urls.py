from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('booking/', views.booking, name='booking'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
]

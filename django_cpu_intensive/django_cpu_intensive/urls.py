from django.urls import path
from . import views

urlpatterns = [
    path('calculate_primes/<int:end>/', views.calculate_primes, name='calculate_primes'),
    path('calculate_primes/concurrent/<int:end>/', views.calculate_primes_concurrent, name='calculate_primes_concurrent'),
    path('calculate_primes/parallel/<int:end>/', views.calculate_primes_parallel, name='calculate_primes_parallel'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('converter/', views.calculate_exchange),
]

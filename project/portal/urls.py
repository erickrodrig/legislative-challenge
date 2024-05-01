from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('bills/', views.bills),
    path('legislators/', views.legislators),
    path('upload/', views.upload),
]

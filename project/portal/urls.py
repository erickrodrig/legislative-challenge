from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('bills/', views.bills, name="bills"),
    path('legislators/', views.legislators, name="legislators"),
    path('upload/', views.upload, name="upload"),
]

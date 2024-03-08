# arithmetic_backend/urls.py
from django.urls import path
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluate/', views.evaluate_expression, name='evaluate_expression'),
]

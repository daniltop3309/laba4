from django.urls import path
from films import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

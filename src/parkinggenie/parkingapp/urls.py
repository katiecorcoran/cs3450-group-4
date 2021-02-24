from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('spaces/<int:space_id>/', views.space, name='space'),
    path('spaces/<int:space_id>/reserve', views.reserve_space, name='reserve_space'),
    path('lots/<int:lot_id>/', views.lot, name='lot')
]
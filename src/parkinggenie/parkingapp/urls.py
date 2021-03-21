from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lots/', views.lots, name='lots'),
    path('spaces/<int:lot_id>/reserve/', views.reserve_space, name='reserve_space'),
    path('lots/<int:lot_id>/', views.lot, name='lot')
]
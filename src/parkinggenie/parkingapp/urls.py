from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lots/', views.lots, name='lots'),
    path('lots/<int:lot_id>/<str:space_type>/reserve/', views.reserve_space, name='reserve_space'),
    path('lots/<int:lot_id>/', views.lot, name='lot')
]
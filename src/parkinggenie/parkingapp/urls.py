from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lots/', views.lots, name='lots'),
    path('spaces/<int:lot_id>/', views.spaces, name='spaces'),
    path('spaces/<int:space_id>/reserve/', views.reserve_space, name='reserve_space'),
    path('lots/<int:lot_id>/', views.lot, name='lot'),
    path('owner/', views.owner, name='owner'),
    path('owner/addinglot', views.addingspace, name='addingspace')
]
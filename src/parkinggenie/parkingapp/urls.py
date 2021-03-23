from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lots/', views.lots, name='lots'),
<<<<<<< HEAD
    path('spaces/<int:lot_id>/', views.spaces, name='spaces'),
    path('spaces/<int:space_id>/reserve/', views.reserve_space, name='reserve_space'),
    path('lots/<int:lot_id>/', views.lot, name='lot'),
]
=======
    path('lots/<int:lot_id>/<str:space_type>/reserve/', views.reserve_space, name='reserve_space'),
    path('lots/<int:lot_id>/', views.lot, name='lot')
]
>>>>>>> 58f5834dc04294ff29adba67307ae90f29a84597

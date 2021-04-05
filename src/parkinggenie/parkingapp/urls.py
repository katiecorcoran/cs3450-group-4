from django.urls import path

from . import views
from .views import LotCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('lots/', views.lots, name='lots'),
    path('lots/<int:lot_id>/', views.lot, name='lot'),
    path('owner/', views.owner, name='owner'),
    path('owner/addinglot/', views.get_TotalSpaces, name='addingspace'),
    path('owner/', views.owner, name='owner'),
    path('lots/<int:lot_id>/<str:space_type>/reserve/', views.reserve_space, name='reserve_space'),
    path('add-lot', LotCreateView.as_view(), name='add-lot'),
    path('signup/', views.signup, name='signup'),
    path('signup/create/', views.create_Account, name='createaccount')
]

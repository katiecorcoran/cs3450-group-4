from django.urls import path, include

from . import views
from .views import ReservationCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('lots/', views.lots, name='lots'),
    path('lots/<int:lot_id>/', views.lot, name='lot'),
    path('owner/', views.owner, name='owner'),
    path('owner/addinglot/', views.get_TotalSpaces, name='addingspace'),
    path('owner/', views.owner, name='owner'),
    path('lots/<int:lot_id>/<str:space_type>/reserve/', views.reserve_space, name='reserve_space'),
    path('signup/', views.signup, name='signup'),
    path('signup/create/', views.create_Account, name='createaccount'),
    path('reservation', views.reserve_space, name='reservation'),
    path('accounts/', include('django.contrib.auth.urls')),
]

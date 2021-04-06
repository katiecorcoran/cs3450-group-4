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
    path('lots/<int:pk>/<str:space_type>/reserve/', ReservationCreateView.as_view()),
    path('reservation-success/<int:id>', views.success, name='reservation-success'),
    path('signup/', views.signup, name='signup'),
    path('signup/create/', views.create_Account, name='createaccount'),
    path('accounts/', include('django.contrib.auth.urls')),
]

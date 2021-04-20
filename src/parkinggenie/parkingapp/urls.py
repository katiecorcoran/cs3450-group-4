from django.urls import path, include

from . import views
from .views import ReservationCreateView, UserAccountView

urlpatterns = [
    path('', views.redirect_index, name='index'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>/', views.lots, name='lots'),
    path('events/lots/<int:lot_id>/', views.lot, name='lot'),
    path('<int:pk>/<str:space_type>/reserve/', ReservationCreateView.as_view(), name='reserve'),
    path('reservation-success/<int:id>', views.success, name='reservation-success'),
    path('owner/', views.owner, name='owner'),
    path('owner/addinglot/', views.get_TotalSpaces, name='addingspace'),
    path('signup/', views.signup, name='signup'),
    path('signup/create/', views.create_Account, name='createaccount'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', UserAccountView.as_view(), name='profilePage'),
    path('addEvent/', views.event, name='event'),
    path('addEvent/addingevent/', views.get_events, name='addingevent'),
]

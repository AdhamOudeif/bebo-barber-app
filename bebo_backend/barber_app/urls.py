from django.urls import path
from .views import AppointmentCreateView, AppointmentDeleteView, AppointmentDetailView, AppointmentListView, AppointmentUpdateView, ServiceCreateView, ServiceDeleteView, ServiceDetailView, ServiceListView, ServiceUpdateView, UserListView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointments/update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment-update'),
    path('appointments/delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment-delete'),
    path('services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('services/update/<int:pk>/', ServiceUpdateView.as_view(), name='service-update'),
    path('services/delete/<int:pk>/', ServiceDeleteView.as_view(), name='service-delete'),
]

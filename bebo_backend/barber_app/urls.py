from django.urls import path
from .views import AppointmentCreateView, AppointmentDeleteView, AppointmentDetailView, AppointmentListView, AppointmentUpdateView, CreatePaymentIntentView, ReviewCreateView, ReviewDeleteView, ReviewDetailView, ReviewListView, ReviewUpdateView, ServiceCreateView, ServiceDeleteView, ServiceDetailView, ServiceListView, ServiceUpdateView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, stripe_webhook

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
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('payments/create-intent/', CreatePaymentIntentView.as_view(), name='create-payment-intent'),
    path('payments/webhook/', stripe_webhook, name='stripe-webhook'),
]

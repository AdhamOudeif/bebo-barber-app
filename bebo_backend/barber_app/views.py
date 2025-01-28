from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from bebo_backend.bebo_backend import settings
from .models import Appointment, Payment, Review, Service, User
from .serializers import AppointmentSerializer, ReviewSerializer, ServiceSerializer, UserSerializer
import stripe

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# User CRUD Logic
class UserUpdateView(APIView):
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data, partial=True)  # `partial=True` allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteView(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Appointments CRUD Logic
class AppointmentCreateView(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentListView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AppointmentDetailView(APIView):
    def get(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AppointmentUpdateView(APIView):
    def put(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)  # Partial allows updating specific fields
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDeleteView(APIView):
    def delete(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        appointment.delete()
        return Response({"message": "Appointment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Services CRUD Logic

class ServiceCreateView(APIView):
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ServiceDetailView(APIView):
    def get(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ServiceUpdateView(APIView):
    def put(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service, data=request.data, partial=True)  # Allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDeleteView(APIView):
    def delete(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

        service.delete()
        return Response({"message": "Service deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Reviews CRUD Logic
    
class ReviewCreateView(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewListView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        barber_id = request.query_params.get('barber_id')
        client_id = request.query_params.get('client_id')

        if barber_id:
            reviews = reviews.filter(barber_id=barber_id)
        if client_id:
            reviews = reviews.filter(client_id=client_id)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReviewDetailView(APIView):
    def get(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReviewUpdateView(APIView):
    def put(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDeleteView(APIView):
    def delete(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response({"message": "Review deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
### PAYMENT LOGIC AND WEBHOOK - Needs Review and integration with stripe properly
stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentIntentView(APIView):
    def post(self, request):
        try:
            appointment_id = request.data.get('appointment_id')
            appointment = Appointment.objects.get(id=appointment_id)

            amount = int(appointment.service.price * 100)  # Convert dollars to cents
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                payment_method_types=['card'],
                metadata={'appointment_id': appointment.id}
            )

            payment = Payment.objects.create(
                appointment=appointment,
                client=appointment.client,
                barber=appointment.barber,
                amount=appointment.service.price,
                payment_method='card',
                payment_status='pending',
                transaction_id=intent.id
            )

            return Response({
                "client_secret": intent['client_secret'],
                "payment_id": payment.id
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        transaction_id = intent['id']
        try:
            payment = Payment.objects.get(transaction_id=transaction_id)
            payment.payment_status = 'successful'
            payment.save()
        except Payment.DoesNotExist:
            pass

    return JsonResponse({'status': 'success'}, status=200)


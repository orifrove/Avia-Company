from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.views.generic import ListView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from apps.flights.models import Flight
from .models import Bookings
from .serializers import BookingsSerializer


class BookingsViewSet(ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['username', 'passport', 'phone', 'flights_id', 'payments_id']
    search_fields = ['username', 'passport', 'phone']
    ordering_fields = ['username', 'flights_id']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsAdminUser()]
        return [IsAuthenticated()]


class BookingListView(ListView):
    model = Bookings
    template_name = 'bookings/list.html'
    context_object_name = 'bookings'


class BookingCreateView(CreateView):
    def get(self, request, flight_pk):
        flight = get_object_or_404(Flight, pk=flight_pk)
        return render(request, 'bookings/create.html', {'flight': flight})

    def post(self, request, flight_pk):
        flight = get_object_or_404(Flight, pk=flight_pk)
        Bookings.objects.create(
            flights_id=flight.pk,
            username=request.POST.get('username'),
            passport=request.POST.get('passport'),
            phone=request.POST.get('phone'),
        )
        messages.success(request, 'Бронирование успешно создано!')
        return redirect('bookings:list')


class BookingDeleteView(DeleteView):
    model = Bookings
    success_url = reverse_lazy('bookings:list')
    template_name = 'bookings/list.html'
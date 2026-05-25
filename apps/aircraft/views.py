from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Flight
from .serializers import FlightSerializer


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['number_of_race', 'flight_date', 'flight_time', 'from_city', 'to_city', 'aircraft_id', 'bookings_id']
    search_fields = ['number_of_race', 'flight_date', 'flight_time', 'from_city', 'to_city']
    ordering_fields = ['number_of_race', 'flight_date', 'flight_time', 'from_city', 'to_city']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        elif self.action == 'destroy':
            return [IsAdminUser()]
        return [IsAuthenticated()]


class FlightListView(ListView):
    model = Flight
    template_name = 'flights/list.html'
    context_object_name = 'flights'
    paginate_by = 6

    def get_queryset(self):
        qs = Flight.objects.all()
        from_city = self.request.GET.get('from_city')
        to_city = self.request.GET.get('to_city')
        flight_date = self.request.GET.get('flight_date')
        if from_city:
            qs = qs.filter(from_city__icontains=from_city)
        if to_city:
            qs = qs.filter(to_city__icontains=to_city)
        if flight_date:
            qs = qs.filter(flight_date=flight_date)
        return qs


class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flights/detail.html'
    context_object_name = 'flight'
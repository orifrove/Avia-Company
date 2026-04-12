from rest_framework.viewsets import ModelViewSet
from .models import Bookings
from .serializers import BookingsSerializer

class BookingsViewSet(ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
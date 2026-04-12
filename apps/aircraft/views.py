from rest_framework.viewsets import ModelViewSet
from .models import Aircraft
from .serializers import AircraftSerializer

class AircraftViewSet(ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

from rest_framework.viewsets import ModelViewSet
from .models import Payments
from .serializers import PaymentsSerializer

class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
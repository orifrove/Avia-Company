from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import FlightViewSet, FlightListView, FlightDetailView

app_name = 'flights'

router = DefaultRouter()
router.register('', FlightViewSet)

urlpatterns = [
    path('', FlightListView.as_view(), name='list'),
    path('<int:pk>/', FlightDetailView.as_view(), name='detail'),
] + router.urls
from rest_framework.routers import DefaultRouter
from .views import AircraftViewSet

router = DefaultRouter()
router.register('', AircraftViewSet)

urlpatterns = router.urls
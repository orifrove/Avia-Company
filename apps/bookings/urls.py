from rest_framework.routers import DefaultRouter
from .views import BookingsViewSet

router = DefaultRouter()
router.register('', BookingsViewSet)

urlpatterns = router.urls
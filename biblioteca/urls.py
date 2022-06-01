from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import PrestamoViewSet

router = routers.DefaultRouter()
router.register('prestamos', PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'gender', GenderViewSet)

urlpatterns = [
    path('', include(router.urls))
]

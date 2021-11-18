from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product-details', ProductDetailsViewSet)
router.register(r'gender', GenderViewSet)
router.register(r'brand', BrandViewSet)

urlpatterns = [
    path('', include(router.urls))
]

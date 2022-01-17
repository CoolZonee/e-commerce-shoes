from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .models import *
from .serializers import *
import json


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        gender = request.GET.get('gender')
        queryset = Product.objects.all().order_by("-date")
        if gender:
            queryset = Product.objects.filter(
                gender__name=gender).order_by("-date")
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        token = request.COOKIES.get('token')
        print(token)
        gender = request.GET.get('gender')
        queryset = Product.objects.all()
        if gender:
            queryset = Product.objects.filter(
                upc=pk, gender__name=gender)
        product = generics.get_object_or_404(queryset, upc=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailsViewSet(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer

    def list(self, request):
        queryset = ProductDetails.objects.all()
        serializer = ProductDetailsRetrieveSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):

        queryset = ProductDetails.objects.filter(product__upc=pk)

        serializer = ProductDetailsRetrieveSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

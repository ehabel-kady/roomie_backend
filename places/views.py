from django.shortcuts import render
from places.models import *
from places.serializers import *
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from math import sin, cos, sqrt, atan2, radians

# Create your views here.

class OffersCreateView(CreateAPIView):
    serializer_class = OfferSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        """
        Preform Create of an offer then return the device instance
        """
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        offer = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class OffersSearchView(CreateAPIView):
    serializer_class = OfferSerializer
    permission_classes = [permissions.AllowAny]

    def get_distance(self, long1, lat1, long2, lat2):
        R = 6373.0
        lat1 = radians(lat1)
        lon1 = radians(long1)
        lat2 = radians(lat2)
        lon2 = radians(long2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance
    def get(self, request, *args, **kwargs):
        if request.data["longtude"]:
            longtude = request.data["longtude"] 
        if request.data['latitude']:
            latitude = request.data['latitude']
        offers = Offer.objects.values()
        final_offers = []
        for offer in offers:
            distance = self.get_distance(offer['longtude'], offer['latitude'], longtude, latitude)
            if distance < 20:
                print(distance)
                final_offers.append(offer)
        return Response({"offers":final_offers}, status=status.HTTP_200_OK)
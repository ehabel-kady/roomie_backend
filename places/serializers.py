from rest_framework import serializers
from places.models import *

class OfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Offer
        fields="__all__"
from rest_framework import serializers
from .models import Listestates

class ListestatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listestates
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'slug',)

class listestatesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listestates
        fields = '__all__'
        lookup_field = 'slug'
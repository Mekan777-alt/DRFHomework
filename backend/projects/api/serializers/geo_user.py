from rest_framework import serializers


class GeoUserSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=255)
    country_name = serializers.CharField(max_length=255)


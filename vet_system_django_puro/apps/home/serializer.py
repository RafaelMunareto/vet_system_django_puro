from rest_framework import serializers
from .models import *

class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'
        
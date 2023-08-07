from rest_framework import serializers
from quotes.models import Quote
from django.contrib.auth.models import User


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password',]

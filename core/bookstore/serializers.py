from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    name= serializers.CharField(required=True, min_length=3, max_length=150)
    class Meta:
        model = Book
        fields = '__all__'
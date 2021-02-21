from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    created = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Author
        fields = ["url", "name", "books", "created"]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True)

    created = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    modified = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    available = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_available(obj):
        return obj.is_available

    @staticmethod
    def get_price(obj):
        return obj.get_price

    class Meta:
        model = Book
        fields = [
            "url",
            "title",
            "description",
            "authors",
            "available",
            "price",
            "created",
            "modified",
        ]

from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """ Author models serializer """

    books = serializers.StringRelatedField(many=True)

    created = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books", "created"]


class BookSerializer(serializers.ModelSerializer):
    """ Book model serializer """

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
            "id",
            "title",
            "description",
            "authors",
            "available",
            "price",
            "created",
            "modified",
        ]

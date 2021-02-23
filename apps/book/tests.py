from django.test import TestCase
from apps.book.models import Book, Author
from apps.book.serializers import AuthorSerializer, BookSerializer
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

# initialize the APIClient app
client = Client()


class BookTestCase(TestCase):
    def setUp(self):
        author_gustavo = Author.objects.create(name="Gustavo Ferreira")
        author_kenneth = Author.objects.create(name="Kenneth S. Rubin")

        book_gatilhos_mentais = Book.objects.create(
            title="Gatilhos Mentais",
            description="O Guia Completo com Estratégias de Negócios e Comunicações Provadas Para Você Aplicar",
            price=28.99,
        )
        book_scrum_essencial = Book.objects.create(
            title="Scrum Essencial",
            description="um Guia Prático Para o Mais Popular Processo ágil",
            price=68.99,
        )

        book_gatilhos_mentais.authors.add(author_gustavo)
        book_scrum_essencial.authors.add(author_kenneth)

    def test_book_create(self):
        author_gustavo = Author.objects.get(name="Gustavo Ferreira")
        author_kenneth = Author.objects.get(name="Kenneth S. Rubin")
        self.assertEqual(author_gustavo.name, "Gustavo Ferreira")
        self.assertEqual(author_kenneth.name, "Kenneth S. Rubin")

        book_gatilhos_mentais = Book.objects.get(title="Gatilhos Mentais")
        book_scrum_essencial = Book.objects.get(title="Scrum Essencial")
        self.assertEqual(book_gatilhos_mentais.title, "Gatilhos Mentais")
        self.assertEqual(book_scrum_essencial.title, "Scrum Essencial")

        self.assertIn(author_gustavo, book_gatilhos_mentais.authors.all())
        self.assertIn(author_kenneth, book_scrum_essencial.authors.all())

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse("book-list"))
        # get data from db
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

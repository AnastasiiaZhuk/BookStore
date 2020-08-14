from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from Books.models import Book, Review
# Create your tests here.


class BookTest(TestCase):
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='Winsotn',
            email='winston111@gmail.com',
            password='234234Nasi'
        )

        self.book = Book.objects.create(
            title='Django for You',
            author='Winston A.',
            price=29.11,
        )

        self.review = Review.objects.create(  # new
            book=self.book,
            author=self.user,
            review='An excellent review',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Django for You')
        self.assertEqual(f'{self.book.author}', 'Winston A.')
        self.assertEqual(f'{self.book.price}', '29.11')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django for You')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/2342/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Django')
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'books/book_detail.html')
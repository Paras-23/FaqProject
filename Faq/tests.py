from django.test import TestCase
from .models import FAQ
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.core.cache import cache
from .serializers import FAQSerializer

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="A web framework.")

    def test_faq_creation(self):
        faq = FAQ.objects.get(question="What is Django?")
        self.assertEqual(faq.answer, "A web framework.")

class FAQAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")

    def test_get_faqs(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "What is Django?")
        
class FAQCacheTestCase(APITestCase):
    def test_cache(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        cache.set(f'faq_{faq.id}', faq)
        cached_faq = cache.get(f'faq_{faq.id}')
        self.assertEqual(cached_faq.question, faq.question)
        

class FAQSerializerTestCase(TestCase):
    def test_valid_serializer(self):
        data = {'question': 'What is Django?', 'answer': 'Django is a web framework.'}
        serializer = FAQSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        data = {'question': '', 'answer': 'Django is a web framework.'}
        serializer = FAQSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class FAQViewTestCase(APITestCase):
    def test_get_faqs(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FAQModelTestCase(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "Django is a web framework.")

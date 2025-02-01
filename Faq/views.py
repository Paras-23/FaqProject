from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        faqs = FAQ.objects.all()
        data = [
            {
                'id': faq.id,
                'question': faq.get_translated_question(lang),
                'answer': faq.answer
            }
            for faq in faqs
        ]

        cache.set(cache_key, data, timeout=3600)  # Cache for 1 hour
        return Response(data, status=status.HTTP_200_OK)

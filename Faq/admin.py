from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'question_hi', 'question_bn', 'question_fr', 'question_es', 'question_de')
    search_fields = ('question', 'question_hi', 'question_bn', 'question_fr', 'question_es', 'question_de')

admin.site.register(FAQ, FAQAdmin)

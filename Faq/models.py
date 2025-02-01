from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    question_fr = models.TextField(blank=True, null=True)
    question_es = models.TextField(blank=True, null=True)
    question_de = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        self.question_hi = self.question_hi or translator.translate(self.question, dest='hi').text
        self.question_bn = self.question_bn or translator.translate(self.question, dest='bn').text
        self.question_fr = self.question_fr or translator.translate(self.question, dest='fr').text
        self.question_es = self.question_es or translator.translate(self.question, dest='es').text
        self.question_de = self.question_de or translator.translate(self.question, dest='de').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question)

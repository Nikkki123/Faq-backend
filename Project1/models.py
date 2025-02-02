# models.py
from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def get_translated_question(self, lang='en'):
        if lang == 'hi':
            return self.question_hi or self.question
        elif lang == 'bn':
            return self.question_bn or self.question
        return self.question

    def save(self, *args, **kwargs):
        # Automatically translate questions on save
        if not self.question_hi:
            self.question_hi = self.translate(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate(self.question, 'bn')
        super().save(*args, **kwargs)

    def translate(self, text, lang):
        from googletrans import Translator
        translator = Translator()
        translated = translator.translate(text, dest=lang)
        return translated.text
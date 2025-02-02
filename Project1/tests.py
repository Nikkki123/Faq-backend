from django.test import TestCase

from .models import FAQ

class FAQModelTest(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(question="Test question", answer="Test answer")
        self.assertEqual(faq.question, "Test question")

    def test_translation(self):
        faq = FAQ.objects.create(question="Hello", answer="World")
        self.assertEqual(faq.get_translated_question('hi'), translate_text("Hello", 'hi'))

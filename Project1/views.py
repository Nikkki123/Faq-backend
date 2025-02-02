from django.shortcuts import render, HttpResponse
from .models import TodoItem 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

# Create your views here.
def home(request):
    return HttpResponse("Hello from Django!")
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html","todos.html",{"todos": items })
@api_view(['GET'])
def getData(request):
    person={'name':'Dennis', 'age':28}
    return response(person)


from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        queryset = self.get_queryset()
        data = []
        for faq in queryset:
            data.append({
                'question': faq.get_translated_question(lang),
                'answer': faq.get_translated_answer(lang)
            })
        return Response(data)
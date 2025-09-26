from django.shortcuts import render
from .models import Yangiliklar
from django.http import HttpRequest
from rest_framework import generics
from .serializers import YangiliklarSerializer
# Create your views here.

def all_news(request):
    news = Yangiliklar.objects.all()
    context = {
        'news':news
    }
    return render(request, 'all_news.html', context)

def detail(request, id):
    yangilik = Yangiliklar.objects.get(id=id)
    context = {
        'yangilik':yangilik
    }
    return render(request, 'detail.html', context)

class YangiliklarList(generics.ListAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer

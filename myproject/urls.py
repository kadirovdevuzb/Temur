from django.urls import path
from .views import all_news, detail

urlpatterns = [
    path('all_news/', all_news, name='news'),
    path('detail/<int:id>/', detail, name='detail') 
]
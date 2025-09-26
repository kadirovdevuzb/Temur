from django.urls import path
from .views import all_news, detail, YangiliklarList, FilmlarList

urlpatterns = [
    path('all_news/', all_news, name='news'),
    path('detail/<int:id>/', detail, name='detail') 
]

urlpatterns += [
    path('yangiliklar-list/', YangiliklarList.as_view(), name='Yangiliklar-list'),
    path('filmlar-api/', FilmlarList.as_view(), name='Filmlar-list')
]
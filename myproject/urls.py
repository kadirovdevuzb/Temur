from django.urls import path
from .views import all_news, detail, YangiliklarList

urlpatterns = [
    path('all_news/', all_news, name='news'),
    path('detail/<int:id>/', detail, name='detail') 
]

urlpatterns += [
    path('yangiliklar-list/', YangiliklarList.as_view(), name='Yangiliklar-list')
]
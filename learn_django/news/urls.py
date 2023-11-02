from . import views
from django.urls import path

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    #Создаем динамический адрес
    path('<int:pk>', views.NewsDetail.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdate.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDelete.as_view(), name='news-delete'),
]
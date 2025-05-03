from django.urls import path

from clubs import views

urlpatterns = [
    path('', views.index, name='main'),
    path('articles/', views.articles, name='articles'),
    path('add_article/', views.add_article, name='add_article'),
]

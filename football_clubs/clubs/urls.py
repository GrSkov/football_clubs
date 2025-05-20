from django.urls import path

from clubs import views

urlpatterns = [
    path('', views.index, name='main'),
    path('article/', views.article, name='article'),
    path('add_article/', views.add_article, name='add_article'),
    path('show_article/<slug:article_slug>/', views.show_article, name='show_article'),
]

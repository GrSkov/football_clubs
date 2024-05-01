from django.urls import path

from clubs import views

urlpatterns = [
    path('', views.index, name='main'),
]

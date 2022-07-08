from django.urls import path

from MAP.map import views

urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path

from films import views

app_name = 'films'

urlpatterns = [
    path('', views.index, name='index'),
    path('films/watched/', views.watched_list, name='watched_list'),
]

from django.urls import path

from . import views

app_name = 'teams'

urlpatterns = [
    path('teams/', views.index, name='index'),
    path('teams/<int:team_id>/', views.detail, name='detail'),
    path('news/<int:news_id>/', views.newsdetail, name='news'),
    path('', views.search, name='search'),
    path('searching', views.searching, name='searching'),
   # path('hh', views.hhdetail, name='hh'),
]

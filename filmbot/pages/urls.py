from django.urls import path
from . import views
from .views import FilmDetailView, FilmListView


urlpatterns = [
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film-detail'),
    path('film/', FilmListView.as_view(), name='film-list'),
    path('statistic', views.statistic_page, name='statistic-page'),
    path('', views.main_page, name='main-page'),
]

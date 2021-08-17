from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from content.models import Film


def main_page(request):
    return render(request, 'pages/main_page.html', {})


class FilmDetailView(DetailView):
    model = Film


class FilmListView(ListView):
    model = Film
    ordering = ['-stat_count_first_places', 'film_name']

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from content.models import Film
from pages.logic import get_stat_dict_for_page, get_stat_dict_in_interval
from .forms import SearchForm
from django.utils import timezone


def main_page(request):
    return render(request, 'pages/main_page.html', {})


def statistic_page(request):
    stat_dict = get_stat_dict_for_page()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            period_data = get_stat_dict_in_interval(start_date, end_date)
            stat_dict = {**stat_dict, **period_data}
    else:
        today = timezone.now()
        yesterday = today - timezone.timedelta(days=1)
        form = SearchForm(initial={'start_date': today, 'end_date': yesterday})
    print(stat_dict)
    stat_dict['form'] = form
    return render(request, 'pages/statistic_page.html', stat_dict)


class FilmDetailView(DetailView):
    model = Film


class FilmListView(ListView):
    model = Film
    ordering = ['-stat_count_first_places', 'film_name']

from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.Form):
    start_date = forms.DateField(
        label='Статистика с', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(
        label='Статистика по', widget=forms.widgets.DateInput(attrs={'type': 'date'}))

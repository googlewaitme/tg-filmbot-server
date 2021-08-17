from rest_framework import viewsets
from .serializers import *
from .models import Dictribution, Film, Activity, Message
from django.utils.timezone import now
from fuzzywuzzy import process


class DictributionViewSet(viewsets.ModelViewSet):
    queryset = Dictribution.objects.all()
    serializer_class = DictributionSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        to_send = query_params.get('to_send', None)
        if to_send:
            return Dictribution.objects.filter(is_send=False, send_time__lte=now())
        return Dictribution.objects.all()  # .filter(is_send=False)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        unique_name = query_params.get('unique_name', None)
        if unique_name:
            message, created = Message.objects.get_or_create(
                unique_name=unique_name,
                defaults={'text': f'Текст для {unique_name} не уставлен!'}
            )
            return [message]
        return Message.objects.all()


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        search_data = query_params.get('search_data', None)
        if search_data:
            films = [film[0] for film in process.extract(search_data, Film.objects.all())]
            return films
        return Film.objects.all()

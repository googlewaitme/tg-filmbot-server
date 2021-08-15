from rest_framework import serializers
from .models import Dictribution, Film, Activity, Message


class DictributionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dictribution
        fields = '__all__'


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

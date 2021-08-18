from content.models import Activity
from django.db import models
from django.utils import timezone


def get_stat_dict_for_page():
    today = timezone.now()
    yesterday = today - timezone.timedelta(days=1)
    last_month = today - timezone.timedelta(days=31)
    stat = {
        'all_users_day': stat_collector('user', yesterday, today),
        'all_messages_day': stat_collector('user', yesterday, today, unique_by_element_id=False),
        'new_users_day': stat_collector('new_user', yesterday, today),
        'all_users_month': stat_collector('user', last_month, today),
        'all_messages_month': stat_collector('user', last_month, today, unique_by_element_id=False),
        'new_users_month': stat_collector('new_user', last_month, today)
    }
    return stat


def get_stat_dict_in_interval(start_date, end_date):
    stat = {
        'all_users_period': stat_collector('user', start_date, end_date),
        'all_messages_period': stat_collector('user', start_date, end_date, unique_by_element_id=False),
        'new_users_period': stat_collector('new_user', start_date, end_date)
    }
    return stat


def stat_collector(activity_type, start_date, end_date, unique_by_element_id=True):
    query = Activity.objects.filter(
        time__range=(start_date, end_date),
        activity_type=activity_type,
    )
    if unique_by_element_id:
        query = query.values('element_unique_id').annotate(n=models.Count('pk'))
    return query.count()

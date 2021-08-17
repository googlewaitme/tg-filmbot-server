from .models import *
from django.contrib import admin


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('film_name', 'url')
    search_fields = ('film_name', 'url')
    ordering = ('film_name', 'url')


@admin.register(Dictribution)
class DictributionAdmin(admin.ModelAdmin):
    list_display = ('name', 'send_time', 'is_send')
    search_fields = ('name',)
    ordering = ('name', 'send_time')
    fieldsets = [
        ('Техническая информация', {
            'fields': ('name', 'send_time', 'is_send')
        }),
        ('Тело рассылки', {
            'fields': (
                'heading_text', 'main_text', 'content_url',
                'button_url', 'button_text')
        })
    ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    def show_text(self, obj):
        return obj.text[:30]

    list_display = ('unique_name', 'show_text')
    search_fields = ('unique_name', 'text')
    ordering = ('unique_name',)

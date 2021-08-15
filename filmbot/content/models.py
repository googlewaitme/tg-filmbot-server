from django.db import models


class Film(models.Model):
    film_name = models.CharField(verbose_name='Название фильма', max_length=200)
    url = models.URLField(verbose_name='Ссылка на скачивание')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.film_name


class Dictirbution(models.Model):
    send_time = models.DateTimeField(verbose_name='Время отправки')
    name = models.CharField(verbose_name='Название рассылки', max_length=200)
    is_send = models.BooleanField(verbose_name='Было отправлено?', default=False)
    heading_text = models.CharField(verbose_name='Заголовок', max_length=200)
    main_text = models.TextField(verbose_name='Текст')
    content_url = models.URLField(verbose_name='Ссылка на контент', null=True, blank=True)
    button_url = models.URLField(verbose_name='Ссылка кнопки', null=True, blank=True)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return self.name + ' ' + str(self.send_time.date())


class Activity(models.Model):
    activity_type = models.CharField(verbose_name='Тип активности', max_length=200)
    element_unique_id = models.CharField(
        verbose_name='Айди элемент активности', max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Активность"
        verbose_name_plural = 'Активности'

    def __str__(self):
        return self.activity_type + ' ' + self.element_unique_id

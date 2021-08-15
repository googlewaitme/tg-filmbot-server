# Generated by Django 3.2.6 on 2021-08-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210815_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictirbution',
            name='heading_text',
            field=models.CharField(default=None, max_length=200, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dictirbution',
            name='button_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка кнопки'),
        ),
        migrations.AlterField(
            model_name='dictirbution',
            name='content_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на контент'),
        ),
        migrations.AlterField(
            model_name='dictirbution',
            name='main_text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]

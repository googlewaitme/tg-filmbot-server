# Generated by Django 3.2.6 on 2021-08-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='unique_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Уникальное название'),
        ),
    ]
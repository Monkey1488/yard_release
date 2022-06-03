# Generated by Django 4.0.4 on 2022-05-31 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Название')),
                ('url', models.CharField(max_length=1000, verbose_name='Ссылка')),
                ('keywords', models.TextField(verbose_name='Ключевые слова')),
                ('start_time', models.TimeField(verbose_name='Время начала')),
                ('end_time', models.TimeField(verbose_name='Время окончания')),
                ('activate', models.BooleanField(verbose_name='Активен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего редактирования')),
            ],
            options={
                'verbose_name': 'Точка',
                'verbose_name_plural': 'Точки',
            },
        ),
    ]

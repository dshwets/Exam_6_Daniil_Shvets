# Generated by Django 2.2 on 2020-08-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('email', models.EmailField(max_length=100, verbose_name='Электронная почта')),
                ('text', models.TextField(max_length=2000, verbose_name='Отзыв')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('status', models.CharField(choices=[('active', ' Активно'), ('blocked', 'Заблокирвано')], default='active', max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('text', models.TextField(verbose_name='Текст комментария')),
            ],
        ),
    ]
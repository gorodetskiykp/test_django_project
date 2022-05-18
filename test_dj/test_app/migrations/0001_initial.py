# Generated by Django 4.0.4 on 2022-05-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст поста')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
    ]

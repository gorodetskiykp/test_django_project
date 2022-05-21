from tabnanny import verbose
from django.db import models


class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста')
    created = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    group = models.ForeignKey('Group', verbose_name='Группа', on_delete=models.SET_NULL, 
                              null=True, blank=True,)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created', ]

    def __str__(self):
        return self.text



class Group(models.Model):
    name = models.CharField('Группа', max_length=50)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name', ]

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    title = models.CharField('Название компании', max_length=40)
    inn = models.CharField('ИНН', max_length=12, blank=True, null=True)
    ogrn = models.CharField('ОГРН', max_length=13, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class CustomUser(AbstractUser):
    pass
    company = models.ForeignKey('Company', default='', on_delete=models.SET_DEFAULT, blank=True, null=True)


class Call(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, max_length=120, default='', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, verbose_name='Категория', blank=True, null=True, default='')
    title = models.CharField('Тема', max_length=50)
    message = models.TextField('Описание проблемы')
    file = models.FileField(upload_to='media', verbose_name='Файл', blank=True, null=True)
    created = models.DateField('Дата создания', auto_now_add=True)
    status = models.ForeignKey('Status', on_delete=models.SET_DEFAULT, verbose_name='Статус', blank=True, null=True, default='')
    deadline = models.DateField('Дата предполагаемого решения', blank=True, null=True)
    verdict = models.TextField('Вердикт', default='', blank=True)
    is_archived = models.BooleanField('Отправлен в архив', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class Category(models.Model):
    title = models.CharField('Название категории', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория обращения'
        verbose_name_plural = 'Категории обращений'


class Status(models.Model):
    title = models.CharField('Название', max_length=32)
    id = models.IntegerField('Id', primary_key=True)
    css_styles = models.CharField('Стили CSS', max_length=512, blank=True, null=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус обращения'
        verbose_name_plural = 'Статусы обращений'

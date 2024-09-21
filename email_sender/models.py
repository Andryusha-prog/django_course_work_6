from django.db import models

from users.models import User


# Create your models here.
class Client(models.Model):
    '''
    Клиенты - это те, кто получает рассылки, а не те, кто создает!!!!
    '''
    email = models.CharField(max_length=150, verbose_name='контактный email')
    name = models.CharField(max_length=150, verbose_name='Ф.И.О.')
    comment = models.TextField(verbose_name='комментарий', blank=True, null=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'


class Message(models.Model):
    topic_mail = models.CharField(max_length=150, verbose_name='Тема письма')
    bode_mail = models.TextField(verbose_name='Тело письма')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
    
    def __str__(self) -> str:
        return f'{self.topic_mail}'


class Mailing(models.Model):
    '''
    Настройка рассылки
    '''
    PERIOD_MAILING = [
        ('day', 'Раз в день'),
        ('week', 'Раз в неделю'),
        ('month', 'Раз в месяц'),
    ]

    STATUS_MAILING = [
        ('create', 'Создана'),
        ('start', 'Запущена'),
        ('stop', 'Завершена'),
    ]

    date_start = models.DateTimeField(verbose_name='дата начала рассылки (первая рассылка)')
    periodic = models.CharField(verbose_name='Периодичность рассылки', choices=PERIOD_MAILING, default='day')
    status = models.CharField(verbose_name='Статус рассылки', choices=STATUS_MAILING, default='create')
    date_end = models.DateTimeField(verbose_name='Дата окончания расылки', null=True, blank=True)

    client = models.ManyToManyField(Client, verbose_name='Клиенты для которых рассылка')

    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name='Сообщение для рассылки')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь-Владелец')

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылки'

    def __str__(self) -> str:
        return f'{self.pk}'


class Attempt(models.Model):
    STATUS_ATTEMPT = [
        ('pos', 'Успешно'),
        ('neg', 'Не успешно'),
    ]

    last_date = models.DateTimeField(verbose_name='Дата и время последней попытки рассылки')
    status = models.CharField(max_length=150, verbose_name='статус рассылки')
    answer = models.CharField(verbose_name='Ответ почтового сервера', blank=True, null=True)

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='попытка рассылки',
                                blank=True, null=True)

    class Meta:
        verbose_name = 'Попытки рассылки'
        verbose_name_plural = 'Попытки расылки'

    def __str__(self) -> str:
        return f'{self.last_date} - {self.status}'

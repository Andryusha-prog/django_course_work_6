from django.db import models

# Create your models here.
class Article(models.Model):
    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, null=True, verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='blog/photo', blank=True, null=True)
    view_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    create_date = models.DateTimeField(verbose_name='дата публикации', blank=True, null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.heading} - {self.create_date}'


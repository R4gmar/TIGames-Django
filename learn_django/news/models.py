from django.db import models


# Создаем нашу таблицу-базу данных с новостями
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    announce = models.CharField('Анонс', max_length=250)
    article = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    # Указываем как будет выводиться объект из базы данных
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    #  Меняем название Articless на Новости
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

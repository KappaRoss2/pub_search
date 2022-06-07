from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    reference = models.CharField('Ссылка на источник', max_length=200)
    access = models.CharField('Информация о доступе', max_length=20)
    authors = models.TextField('Список авторов')

    def __str__(self):
        return self.title

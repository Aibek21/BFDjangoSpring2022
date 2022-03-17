from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'
        ordering = ['-name']

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    publication_date = models.DateTimeField(null=True, blank=True)
    num_pages = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.id}: {self.title}'

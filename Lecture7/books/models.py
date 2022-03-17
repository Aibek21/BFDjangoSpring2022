import uuid
from django.db import models

from utils.constants import USER_TYPES, SUPERADMIN


class City(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=500, default='Алматы', unique=True)
    population = models.IntegerField()
    status = models.PositiveSmallIntegerField(choices=USER_TYPES, default=SUPERADMIN)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Author(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True, verbose_name='Название')
    address = models.CharField(max_length=500, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'
        ordering = ['-name']
        unique_together = ['name', 'website']

    def __str__(self):
        return f'{self.id}: {self.name}'


class BookManager(models.Manager):

    def get_by_publisher_with_relation(self, publisher_id):
        return self.get_related().filter(publisher_id=publisher_id)

    def get_by_publisher_without_relation(self, publisher_id):
        return self.filter(publisher_id=publisher_id)

    def get_related(self):
        return self.select_related('publisher')


class BookQuerySet(models.QuerySet):

    def get_by_publisher_with_relation(self, publisher_id):
        return self.get_related().filter(publisher_id=publisher_id)

    def get_by_publisher_without_relation(self, publisher_id):
        return self.filter(publisher_id=publisher_id)

    def get_related(self):
        return self.select_related('publisher')

    def get_by_author(self, author_id):
        return self.get_related().filter(author_id=author_id)

    def get_related(self):
        return self.select_related('author', 'publisher')


class Book(models.Model):
    title = models.CharField(max_length=500, null=True)
    publication_date = models.DateTimeField(null=True, blank=True)
    num_pages = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    authors = models.ManyToManyField(Author)
    publisher = models.OneToOneField(Publisher, on_delete=models.PROTECT, null=True, blank=True)

    # objects = BookManager()

    objects = BookQuerySet.as_manager()

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.id}: {self.title}'

    def check_num_pages(self):
        if self.num_pages > 10:
            return True
        return False

    @classmethod
    def active_books(cls):
        cls.objects.filter(is_active=True)

    @staticmethod
    def compare_books(b1, b2):
        return b1.num_pages > b2.num_pages

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'publication_date': self.publication_date,
            'is_active': self.is_active
        }

    def to_json_detail(self):
        return {
            'id': self.id,
            'title': self.title,
            'publication_date': self.publication_date,
            'is_active': self.is_active,
            'num_pages': self.num_pages
        }

from django.contrib import admin
from books.models import Author, Publisher, Book, City


# admin.site.register(Author)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website', 'city', 'country',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'publisher',)
    list_filter = ('num_pages', 'publisher',)
    search_fields = ('title',)
    ordering = ('-id',)

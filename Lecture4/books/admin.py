from django.contrib import admin
from books.models import Author, Publisher, Book


# admin.site.register(Author)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website', 'city', 'country',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'author', 'publisher',)
    list_filter = ('num_pages', 'author', 'publisher',)
    search_fields = ('title', 'author__first_name', 'author__last_name')
    ordering = ('-id',)

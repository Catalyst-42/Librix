from django.contrib import admin

from .models import Book, Genre, Author, Translator, Translation

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'genre',
        'published_date'
    )
    search_fields = (
        'title',
        'author'
    )

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Translator)
admin.site.register(Translation)
admin.site.register(Book, BookAdmin)


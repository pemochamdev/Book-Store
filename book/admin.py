from django.contrib import admin

from book.models import Category, Book

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name','active', 'created', 'updated')
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('-created',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    '''Admin View for Book'''

    
    list_display = ('name','amount', 'created', 'updated')
    search_fields = ('name',)
    ordering = ('-created',)
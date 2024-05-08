from django.db import models

# Create your models here.

class Category(models.Model):
    '''Model definition for Category.'''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        '''Meta definition for Category.'''

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    '''Model definition for Book.'''

    name = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='book-store')
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='book')


    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    class Meta:
        '''Meta definition for Book.'''

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name
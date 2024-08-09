from django.db import models

class Buku(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    published_date = models.DateField()
    # publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    # cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    # category = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

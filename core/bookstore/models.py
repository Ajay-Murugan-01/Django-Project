from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=1255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    publish_date = models.DateTimeField(auto_now=True)

    # class Meta:
    #     db_table = 'book'
    #     verbose_name_plural = 'Book'

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=230)
    book_price = models.IntegerField()

    book_image = models.ImageField(upload_to='')

    class Meta:
        db_table = 'book_table'
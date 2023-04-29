from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)
    publisher_age = models.IntegerField()
    page_number = models.IntegerField()
    publish_date = models.DateField()
    sci_fi = models.BooleanField(default=False)
    drama = models.BooleanField(default=False)
    novel = models.BooleanField(default=False)

    def __str__(self):
        return self.name

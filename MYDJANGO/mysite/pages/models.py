from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField(verbose_name='Last Updated')
    bodytext = models.TextField('Page content ', blank=True)
# Create your models here.
    def __str__(self):
             return self.title
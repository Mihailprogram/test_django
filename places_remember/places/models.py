from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    latitude = models.FloatField()
    longitude = models.FloatField()
    comment = models.CharField(max_length=255, verbose_name='Коментарий')

    def __str__(self):
        return self.name

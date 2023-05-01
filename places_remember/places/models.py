from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Place(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    latitude = models.FloatField()
    longitude = models.FloatField()
    comment = models.CharField(max_length=255, verbose_name='Коментарий')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,   
    )

    def __str__(self):
        return self.name

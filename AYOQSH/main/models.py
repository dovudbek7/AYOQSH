from django.db import models
from django.apps import AppConfig
from django.urls import reverse


class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class City(models.Model):
    city_name = models.CharField("City_name", max_length=50)
    url = models.CharField("Servise_name", max_length=50)
    fuel1 = models.CharField('ai_80', max_length=50, default='')
    fuel2 = models.CharField('ai_90', max_length=50, default='')
    fuel3 = models.CharField('ai_91', max_length=50, default='')
    fuel4 = models.CharField('ai_92', max_length=50, default='')
    fuel5 = models.CharField('ai_98', max_length=50, default='')

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "City"

    def __str__(self):
        return self.city_name

    def __str__(self):
        return self.servise_name

    # def get_absolute_url(self):
    #     return reverse("filter", kwargs={"slug": self.url})

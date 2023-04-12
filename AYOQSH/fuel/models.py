from django.db import models


from django.urls import reverse


class Fuel(models.Model):
    city_name = models.CharField("City_name", max_length=50)
    url = models.SlugField(max_length=100, unique=True)
    company_name = models.CharField("Company_name", max_length=50)
    fuel1 = models.CharField('AI-80', max_length=50, default='')
    fuel2 = models.CharField('AI-90', max_length=50, default='')
    fuel3 = models.CharField('AI-91', max_length=50, default='')
    fuel4 = models.CharField('AI-92', max_length=50, default='')
    fuel5 = models.CharField('AI-95', max_length=50, default='')

    
    class Meta:
        verbose_name = "Fuel"
        verbose_name_plural = "Fuel"

    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.url})

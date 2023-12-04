from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField (upload_to=None)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
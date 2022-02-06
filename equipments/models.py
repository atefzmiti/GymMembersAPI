from django.db import models


class equipment(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=2083)
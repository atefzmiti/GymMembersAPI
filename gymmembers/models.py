from django.db import models
from datetime import timezone


class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    discipline = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add = True)
    end_date = models.DateField(null=True)
    email = models.EmailField(max_length=200)

from django.db import models
from django.utils import timezone

class Space(models.Model):
    name = models.CharField(max_length=200)
    tags = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

from django.db import models


class Quote(models.Model):
    said_by = models.CharField(max_length=100)
    quote = models.TextField()

    def __str__(self):
        return self.quote

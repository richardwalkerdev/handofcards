from django.db import models


class Hand(models.Model):
    total = models.IntegerField(null=True)
    created = models.DateTimeField()

    # Pretty administration titles
    def __str__(self):
        return str(self.total)
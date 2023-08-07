from django.db import models


class Quote(models.Model):
    title = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

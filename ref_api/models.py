from django.db import models


class Chromosome(models.Model):
    name = models.TextField(default='')
    sequence = models.TextField()
    is_circular = models.IntegerField(default=0)
    trunc512 = models.TextField()
    md5 = models.TextField()
    size = models.IntegerField()

    def __str__(self):
        return self.name

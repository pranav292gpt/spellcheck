from django.db import models

class WordFrequency(models.Model):
    word = models.CharField(max_length=64)
    frequency = models.IntegerField()

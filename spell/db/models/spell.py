from django.db import models

class WordFrequency(models.Model):
    word = models.CharField(max_length=64, db_index=True)
    frequency = models.IntegerField()

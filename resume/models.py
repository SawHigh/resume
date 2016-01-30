from django.db import models

class Resume(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField()
    link = models.URLField()


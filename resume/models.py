from django.db import models

conditions = (("mobile","mobile"),("desktop","desktop"),("both","both"))

class Resume(models.Model):
    title = models.CharField(max_length=200)
    condition = models.CharField(max_length=10, choices=conditions, null=True)
    description = models.TextField()
    published_date = models.DateField()
    link = models.URLField()


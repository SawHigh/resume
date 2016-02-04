# _*_ coding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import User
conditions = (("mobile","mobile"),("desktop","desktop"),("both","both"))

sex_choice = (("MAN", "man"),("WOMEN", "women"),("OTHER", "othrer"))
degrees = (
           (1, u"了解"),
           (2, u"熟悉"),
           (3, u"掌握"),
           (4, u"精通"),
           (5, u"专家"),
           )

class Project(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=200)
    condition = models.CharField(max_length=10, choices=conditions, null=True)
    description = models.TextField()
    published_date = models.DateField(null=True, blank=True)
    link = models.URLField()
    source_code = models.URLField(null=True, blank=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=sex_choice, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    introducion = models.TextField(null=True, blank=True)
    
class Contact(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    link = models.URLField()
    
class Skill(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    degree = models.IntegerField()
    
class Education(models.Model):
    user = models.OneToOneField(User)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=200)
    

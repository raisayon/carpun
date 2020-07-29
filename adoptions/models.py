from django.db import models

# Create your models here.

class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')] #() tuple
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES,blank=True)
    submission_date = models.DateTimeField()
    age = models.ImageField(null=True)
    vaccinations = models.ManyToManyField('Vaccine',blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
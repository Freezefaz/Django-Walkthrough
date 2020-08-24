from django.db import models

# Create your models here.
# Class is one table
# 1 instance of book class represents one row

# model is the one imported, Model is already in django
# ctrl click on models to go to specific place
class Book(models.Model):
    # what are their columns
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)

    # to string
    def __str__(self):
        return self.title

class Publisher(models.Model):
    # what fields
    name = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name +  " - " + self.email

class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    date_of_birth = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


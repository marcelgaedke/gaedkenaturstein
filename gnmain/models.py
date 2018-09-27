from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Picture(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture_title = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.picture_title



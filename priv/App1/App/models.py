from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_html_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Picture(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    alt = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title
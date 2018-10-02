from django.contrib import admin
from .models import Category, Picture, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Picture)
admin.site.register(Post)

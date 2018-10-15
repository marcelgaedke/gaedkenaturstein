from rest_framework import serializers
from .models import Category, Picture, Post

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        #fields = ('category_name')
        fields = '__all__'



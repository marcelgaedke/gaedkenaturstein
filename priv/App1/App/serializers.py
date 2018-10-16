from rest_framework import serializers
from .models import Category, Picture, Post

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        #fields = ('category_name')
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','category','position','title')
        #fields = '__all__'


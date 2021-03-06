'''from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("GN Main")

'''
#from django.contrib.auth.models import User, Group

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import os
from django.conf import settings

from .models import Category, Picture, Post

#For REST API
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from rest_framework import viewsets
from App.serializers import *

class IndexView(generic.ListView):
    model=Category
    template_name = 'App/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        path2 = "App/pictures/Home/"
        if settings.IS_SERVER:
            path = os.path.join(settings.STATIC_ROOT, path2)
        else:
            path = os.path.join(settings.MEDIA_ROOT, path2)
            #path = os.path.join(settings.STATIC_ROOT, path2)
        path_slider = "slider/"
        sliderfilelist = os.listdir(path + path_slider)  # Get Gallery Pictures
        slider_img_list = []
        index=0
        for f in sliderfilelist:
            if "." in f:
                i = f.index(".")
                if (f[i:]==".jpeg")or(f[i:]==".jpg"):
                    file = {'filename': (path2 + path_slider + f), 'description': f[:i], 'index':index}
                    slider_img_list.append(file)
                    index+=1

        context['slider_img_list'] = slider_img_list

        cat = {'category_name': "Home", 'category_html_name':"Home",'id':1}
        context['cat'] = cat
        context['category'] =cat

        return context



class DetailView(generic.DetailView):
    model = Category
    template_name = 'App/category.html'


    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        cat = context['category']
        #path1 = "/var/www/ssd1400/htdocs/App1/static/"
        #path1 = "/home/kidneybean/PycharmProjects/gaedkenaturstein/gnmain/static/"
        #path1 ="/home/kidneybean/Downloads/grabmalehamburg_3_10_18/htdocs/App1/static/"
        #path1 = STATIC_ROOT

        path2 = "App/pictures/"+ cat.category_name +"/"
        #path2 = "gnmain/pictures/"+ cat.category_name +"/"
        #path = path1 + path2
        if settings.IS_SERVER:
            path = os.path.join(settings.STATIC_ROOT, path2)
        else:
            path = os.path.join(settings.MEDIA_ROOT, path2)
            #path = os.path.join(settings.STATIC_ROOT, path2)
        filelist = os.listdir(path)                                 #Get Gallery Pictures
        img_list=[]
        for f in filelist:
            if "." in f:
                i = f.index(".")
                file ={'filename':(path2+f),'description':f[:i]}
                print(f)
                img_list.append(file)

        context['category_list'] = Category.objects.all()
        context['img_list'] = img_list

                                                                    #Get Slider Pictures
        path_slider = "slider/"
        sliderfilelist = os.listdir(path+path_slider)  # Get Gallery Pictures
        slider_img_list = []
        index=0
        for f in sliderfilelist:
            if "." in f:
                i = f.index(".")
                if (f[i:] == ".jpeg") or (f[i:] == ".jpg"):
                    file = {'filename': (path2 + path_slider + f), 'description': f[:i], 'index':index}
                    slider_img_list.append(file)
                    index+=1

        context['slider_img_list'] = slider_img_list


        return context


class ImpressumView(generic.ListView):
    model = Category
    template_name = 'App/impressum.html'


################REST APIs

class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer

'''class CategoryList(APIView):

    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class PostList(APIView):

    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

'''

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, pk=None):    #overwrite the delete method
        pass



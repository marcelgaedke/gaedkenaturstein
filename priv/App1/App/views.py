'''from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("GN Main")

'''

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import os
from django.conf import settings

from .models import Category, Picture, Post


class IndexView(generic.ListView):
    model=Category
    #template_name = 'gnmain/index.html'
    template_name = 'App/index.html'



class DetailView(generic.DetailView):
    model = Category
    #template_name = 'gnmain/category.html'
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
        filelist = os.listdir(path)
        img_list=[]
        for f in filelist:
            if "." in f:
                i = f.index(".")
                file ={'filename':(path2+f),'description':f[:i]}
                img_list.append(file)

        context['category_list'] = Category.objects.all()
        context['img_list'] = img_list
        return context



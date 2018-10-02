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

from .models import Category, Picture, Post


class IndexView(generic.ListView):
    model=Category
    template_name = 'gnmain/index.html'
    #template_name = 'App/index.html'



class DetailView(generic.DetailView):
    model = Category
    template_name = 'gnmain/category.html'
    #template_name = 'App/category.html'

    #path = os.path.join(settings.MEDIA_ROOT, dir_name)




    def get_context_data(self, **kwargs):
        #img_list = os.listdir("/var/www/ssd1400/htdocs/App1/static/App/pictures/Header")
        img_list = os.listdir("/home/kidneybean/PycharmProjects/gaedkenaturstein/gnmain/static/gnmain/pictures/Header")
        context = super(DetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['img_list'] = img_list
        return context



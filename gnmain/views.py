'''from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("GN Main")

'''

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Category, Picture


class IndexView(generic.ListView):
    model=Category
    template_name = 'gnmain/index.html'
    #context_object_name = 'latest_question_list'

class DetailView(generic.DetailView):
    model = Category
    template_name = 'gnmain/category.html'



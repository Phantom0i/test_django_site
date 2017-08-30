from django.shortcuts import render

# Create your views here.
from django.views import generic

from gallery.models import ImgModel


class IndexView(generic.DetailView):
    model = ImgModel

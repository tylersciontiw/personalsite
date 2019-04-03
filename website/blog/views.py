from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import BlogPost


class HomePage(TemplateView):
	template_name = 'home.html'

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import BlogPost


class HomePage(TemplateView):
	template_name = 'home.html'

class Contact(TemplateView):
	template_name = 'contact.html'

class About(TemplateView):
	template_name = 'about.html'

class Portfolio(TemplateView):
	template_name = 'portfolio.html'

class Resume(TemplateView):
	template_name = 'resume.html'

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'
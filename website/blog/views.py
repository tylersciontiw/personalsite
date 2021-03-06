from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import TemplateView
from .models import BlogPost, Project
from .forms import ContactForm


class HomePage(TemplateView):
	template_name = 'home.html'

class Contact(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

class About(TemplateView):
	template_name = 'about.html'

class Portfolio(ListView):
	model = Project
	template_name = 'portfolio.html'

class Resume(TemplateView):
	template_name = 'resume.html'

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'

class BlogPostView(DetailView):
	model = BlogPost
	slug_field = 'slug'
	slug_url_kwarg = 'model_slug'
	template_name = 'post.html'
	context_object_name = 'post'


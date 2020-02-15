from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    path('', views.HomePage.as_view(), name='home'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('about', views.About.as_view(), name='about'),
    path('portfolio', views.Portfolio.as_view(), name='portfolio'),
    path('resume', views.Resume.as_view(), name='resume'),
    path('blog', views.BlogListView.as_view(), name='blog'),
    path('post/<int:pk>', views.BlogPostView.as_view(), name='post'),
]

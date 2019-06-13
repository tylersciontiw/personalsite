from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('about', views.About.as_view(), name='about'),
    path('portfolio', views.Portfolio.as_view(), name='portfolio'),
    path('resume', views.Resume.as_view(), name='resume'),
    path('blog', views.BlogListView.as_view(), name='blog'),
]

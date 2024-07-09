from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pages/contact.html', views.contact, name='contact'),
    path('pages/about.html', views.about, name='about'),
    path('pages/portfolio.html', views.blog, name='portfolio'),
    path('pages/gallery.html', views.gallery, name='gallery'),
]
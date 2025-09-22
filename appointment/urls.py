from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about_view, name='about_html'),
    path('contact.html/', views.contact_view, name='contact_html'),
    path('services.html/', views.services_view, name='services_html'),
    path('dsignupaction/', views.dsignupaction, name='dsignupaction'),
    path('dloginaction/', views.dloginaction, name='dloginaction'),
    path('dviewprofile/', views.dviewprofile, name='dviewprofile'),
    path('dlogoutaction/',views.dlogoutaction,name='dlogoutaction'),
    path('doctorhome/',views.doctorhome,name='doctorhome'),
    path('psignupaction/', views.psignupaction, name='psignupaction'),
    path('ploginaction/', views.ploginaction, name='ploginaction'),
    path('pviewprofile/', views.pviewprofile, name='pviewprofile'),
    path('plogoutaction/',views.plogoutaction,name='plogoutaction'),
    path('patienthome/',views.patienthome,name='patienthome'),


]




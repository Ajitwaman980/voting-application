from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vote/', views.vote, name='vote'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.thank_you, name='thank_you'), 
    path('Privacy_Policy/', views.Privacy_Policy, name='Privacy_Policy'),
]

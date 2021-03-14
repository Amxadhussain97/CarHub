from django.contrib import admin
from django.urls import path
from pages import views
#app_name = "pages"
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
]

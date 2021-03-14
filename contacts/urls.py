from django.urls import path
from . import views
#app_name = "pages"
urlpatterns = [
  path('inquiry/',views.inquiry,name='inquiry'),
]

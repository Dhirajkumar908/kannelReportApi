
from django.urls import path
from kannel import views


urlpatterns = [
   path("",views.home, name='home'),
   path('kannel', views.kannel, name='kannel')
]

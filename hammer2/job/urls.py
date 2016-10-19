from django.conf.urls import include, url

from job import views

urlpatterns = [	

    url(r'^$',  views.index, name='index'), 
    url(r'^index/', views.index, name='index'),
    url(r'^script/', views.script, name='script'),
    url(r'^post_new/', views.post_new, name='post_new'),
]

  

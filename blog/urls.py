from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^main/', views.main, name='main'),
    url(r'^galery/', views.main, name='main'),
    url(r'^about/', views.about, name='about'),
    url(r'^post/', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^events/', views.event_list, name='post_list'),
    url(r'^events/(?P<pk>\d+)/$', views.event_detail, name='post_detail'),
    url(r'^events/new/$', views.event_new, name='post_new'),
    url(r'^events/(?P<pk>\d+)/edit/$', views.event_edit, name='post_edit'),
]
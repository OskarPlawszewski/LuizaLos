from django.conf.urls import url
from . import views
import galery.views
import events.views

urlpatterns = [
    url(r'^$', galery.views.photo_latest, name='main'),
    url(r'^main/', views.main, name='main'),
    # url(r'^galery/', views.main, name='main'),
    url(r'^about/', views.about, name='about'),

    url(r'^post/', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^events/', events.views.event_list, name='post_list'),
    url(r'^events/(?P<pk>\d+)/$', events.views.event_detail, name='post_detail'),
    url(r'^events/new/$', events.views.event_new, name='post_new'),
    url(r'^events/(?P<pk>\d+)/edit/$', events.views.event_edit, name='post_edit'),

    url(r'^galery/', galery.views.photo_list, name='photo'),
]
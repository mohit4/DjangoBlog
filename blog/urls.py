# django core
from django.conf.urls import url

# user defined
from . import views

app_name = 'blog'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^create_post/$', views.PostCreateView.as_view(), name='create_post'),

    url(r'^list_posts/$', views.PostListView.as_view(), name='list_posts'),

    url(r'^post_details/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_details'),

    url(r'^post_update/(?P<pk>[0-9]+)/$', views.PostUpdateView.as_view(), name='post_update'),

    url(r'^post_delete/(?P<pk>[0-9]+)/$', views.PostDeleteView.as_view(), name='post_delete'),
]
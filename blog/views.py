# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django core
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

# user defined
from .models import Post

class IndexView(TemplateView):
    '''
    For homepage
    '''
    template_name = 'blog/index.html'

#############################################
# Model CRUD Views
#############################################

class PostCreateView(CreateView):
    '''
    For creating new post
    '''
    fields = ('title','text')
    model  = Post
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

#############################################

class PostUpdateView(UpdateView):
    '''
    For updating an existing view
    '''
    fields = ('title','text')
    model = Post
    template_name = "blog/post_form.html"

#############################################


class PostDeleteView(DeleteView):
    '''
    For deleting an existing view
    '''
    model = Post
    success_url = reverse_lazy('blog:list_posts')

#############################################

class PostListView(ListView):
    '''
    For listing all posts
    '''
    context_object_name = 'posts'
    model = Post
    template_name = 'blog/post_list.html'

#############################################

class PostDetailView(DetailView):
    '''
    For displaying detailed view of the post
    '''
    model = Post
    template_name = "blog/post_detail.html"
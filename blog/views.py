# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django core
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

# user defined
from .models import Post
# from .decorators import user_required

class IndexView(TemplateView):
    '''
    For homepage
    '''
    template_name = 'blog/index.html'

#############################################
# Model CRUD Views
#############################################

# @method_decorator(login_required, name='dispatch')
class PostCreateView(SuccessMessageMixin, CreateView):
    '''
    For creating new post
    '''
    fields = ('title','text')
    model  = Post
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:index')
    success_message = 'New Post created successfully!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

#############################################

# @method_decorator(login_required, name='dispatch')
# @method_decorator(user_required, name='dispatch')
class PostUpdateView(SuccessMessageMixin, UpdateView):
    '''
    For updating an existing view
    '''
    fields = ('title','text')
    model = Post
    template_name = "blog/post_form.html"
    success_message = 'Post updated successfully!'

#############################################

# @method_decorator(login_required, name='dispatch')
# @method_decorator(user_required, name='dispatch')
class PostDeleteView(SuccessMessageMixin, DeleteView):
    '''
    For deleting an existing view
    '''
    model = Post
    success_url = reverse_lazy('blog:list_posts')
    success_message = 'Post deleted!'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

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
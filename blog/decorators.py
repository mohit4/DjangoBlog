# django core
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect

# user defined
from .models import Post

def login_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'You must be logged in to perform that action!')
            return redirect('blog:index')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_required(function):
    def wrap(request, *args, **kwargs):
        try:
            post = Post.objects.get(pk=kwargs['pk'])
            if post.user == request.user:
                return function(request, *args, **kwargs)
            else:
                messages.error(request, 'You are not authorized to perform this action!')
                return redirect('blog:index')
        except Post.DoesNotExist:
            messages.error(request, 'Post does not exist!')
            return redirect('blog:index')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
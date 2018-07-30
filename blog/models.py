# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Post(models.Model):
    '''
    Structure of a blog post
    '''
    title = models.CharField(max_length = 100)
    text = models.TextField()
    user = models.ForeignKey(User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_details', kwargs={'pk': self.pk})
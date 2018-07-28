# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django core
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    '''
    For homepage
    '''
    template_name = 'blog/index.html'
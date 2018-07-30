# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django core
from django.contrib import admin

# user defined
from .models import Post

# Register your models here.
admin.site.register(Post)
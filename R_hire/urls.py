#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-01-19 02:23:33

from django.conf.urls import url, include, patterns

from . import views

app_name = 'r_hire'
urlpatterns = [
	# ex: /r-hire/
	url(r'^$', views.index, name='index'),
	# ex /r-hire/register/
	url(r'^register/', views.register, name='register'),
]

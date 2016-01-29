#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-30 02:10:08

from django.conf.urls import url, include, patterns

from . import views

app_name = 'r_hire'
urlpatterns = [
	# ex: /r-hire/
	url(r'^$', views.index, name='index'),
	
	# ex: /r-hire/register/
	url(r'^register/$', views.register, name='register'),
	
	# ex: /r-hire/login/
	url(r'^login/$', views.login, name='login'),

	# ex: /r-hire/logout/
	url(r'^logout/$', views.logout, name='logout'),

	# ex: /r-hire/profile/
	url(r'^profile/$', views.viewProfile, name='view-profile'),

	# ex: /r-hire/profile/edit
	url(r'^profile/edit$', views.editProfile, name='edit-profile'),

	# ex: /r-hire/profile/save
	url(r'^profile/update$', views.updateProfile, name='update-profile'),
]

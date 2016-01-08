#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-01-08 23:00:57


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	# render the index.html
	return render(request, 'R_hire/index.html', {})

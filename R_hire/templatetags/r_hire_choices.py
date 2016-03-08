# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-03-09 01:56:45
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-03-09 02:02:34


from django import template

register = template.Library()

@register.filter
def widget_type(ob):
	return ob.__class__.__name__

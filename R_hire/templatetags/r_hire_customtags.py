# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-03-09 02:28:30
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-03-09 02:47:17

from django import template

register = template.Library()

@register.filter
def widget_type(ob):
	return ob.__class__.__name__


@register.inclusion_tag('', takes_context=True)
def render_name(first_name, last_name):
    if last_name is not None :
        name = first_name + last_name
    else :
        name = first_name
    return {'name': name}

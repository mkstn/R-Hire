#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-18 23:49:13

from django.http import HttpResponse
from django.shortcuts import render

# Import the RegistrationForm class from the forms.py in the same module
from .forms import RegistrationForm


def index(request):
	# render the index.html
	return render(request, 'R_hire/index.html', {})


def register(request):
	# If the request method is POST, it means that the form has been submitted
	# and we need to validate it
	if request.method == "POST":
		# Create a RegistrationForm instance with the submitted data
		form  = RegistrationForm(request.POST)

		# is_valid validates a form and returns
		# True if it is valid and
		# False if it is invalid
		if form.is_valid():
			# TODO: The form is valid and we can save it to the database
			# by creating a model object and populating the data from the form object

			# as of now just rendering a success template page
			return render(request, "R_hire/registration/success.html")
	# This means that the request is a GET request. So we need to
	# create an instance of the RegistrationForm class and render it in the template
	else:
		form = RegistrationForm()

	# Render the registration form template with a RegistrationForm instance. If the
	# form was submitted and the data found to be invalid, the template will
	# be rendered with the entered data and error messages. Otherwise an empty
	# form will be rendered.
	return render(request, "R_hire/registration/registration_form.html", {"form" : form})

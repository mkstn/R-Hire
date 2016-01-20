#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-21 04:51:41

from django.http import HttpResponse, HttpResponse
from django.shortcuts import render

# Import the RegistrationForm, LoginForm classes from the forms.py in the same module
from .forms import RegistrationForm, LoginForm

# Import Candidate model from the same module
from .models import Candidate


def index(request):
	# render the index.html
	return render(request, 'R_hire/index.html', {})


def register(request):
	# If the request method is POST, it means that the form has been submitted
	# and we need to validate it
	if request.method == "POST":
		# Create a RegistrationForm instance with the submitted data
		form = RegistrationForm(request.POST)

		# is_valid validates a form and returns
		# True if it is valid and
		# False if it is invalid
		if form.is_valid():			
			first_name	= request.POST['fname']
			last_name 	= request.POST['lname']
			email 		= request.POST['email']
			password 	= request.POST['password']

			# Make an old_candidate object to check whether 
			# email id has already been used or not
			old_candidate = Candidate.objects.filter(email = email)

			# if no candidate has used this email id then register the candidate
			# else throw an error
			if old_candidate.count() == 0:
				new_candidate = Candidate(
					fname 		= first_name,
					lname 		= last_name,
					email		= email,
					password	= password,
				)

				new_candidate.save()

				return render(request, "R_hire/registration/success.html")
			else :
				form.add_error(None, 'Email ID already exists')

	# This means that the request is a GET request. So we need to
	# create an instance of the RegistrationForm class and render it in the template
	else:
		form = RegistrationForm()

	# Render the registration form template with a RegistrationForm instance. If the
	# form was submitted and the data found to be invalid, the template will
	# be rendered with the entered data and error messages. Otherwise an empty
	# form will be rendered.
	return render(request, "R_hire/registration/registration_form.html", {"form" : form})


def login(request):
	# If the request method is POST, it means that the form has been submitted
	# and we need to validate it
	if request.method == "POST":
		# Create a LoginForm instance with the submitted data
		form = LoginForm(request.POST)

		# is_valid validates a form and returns
		# True if it is valid and
		# False if it is invalid
		if form.is_valid():
			email 		= request.POST['email']
			password 	= request.POST['password']

			# Make an check_candidate object to check whether 
			# email id and password make up a valid combination
			check_candidate = Candidate.objects.filter(
				email = email,
				password = password,
			)

			# if combination is not correct then throw an error
			# else login the candidate
			if (check_candidate.count() != 1) :
				form.add_error(None, 'Invalid email - password combination')
			else:
				# TO DO
				# add session control functions here
				# since candidate exists 
				form.add_error(None, 'Logged in')

	# This means that the request is a GET request. So we need to
	# create an instance of the LoginForm class and render it in the template
	else:
		form = LoginForm()

	# Render the login form template with a LoginForm instance. If the
	# form was submitted and the data found to be invalid, the template will
	# be rendered with the entered data and error messages. Otherwise an empty
	# form will be rendered.
	return render(request, "R_hire/registration/login_form.html", {"form" : form})

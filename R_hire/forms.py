#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-18 22:57:52
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-03-09 00:04:54

from django import forms
from django.utils.translation import ugettext_lazy as _

# Import Candidate model from the same module
from .models import Candidate

GENDER_LIST = (	('M', _('Male')),
				('F', _('Female')),
				('ND', _('Not Defined')),
				)

class RegistrationForm(forms.Form):
	fname = forms.CharField(label='First name', max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	lname = forms.CharField(label='Last name', max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)

	email = forms.EmailField(label='Enter your email', widget=forms.EmailInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label='Enter your password')
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Should be same as password field, obviously'}), label='Confirm password')

	# clean_<fieldname> method in a form class is used to do custom validation for the field.
	# We are doing a custom validation for the 'email' field and raising
	# a validation error if the email already exists in the database
	# 
	# Read this link to know more about this method - https://docs.djangoproject.com/en/1.9/ref/forms/validation/#raising-validationerror
	def clean_email(self):
		try:
			candidate = Candidate.objects.get(email__iexact=self.cleaned_data['email'])
		except Candidate.DoesNotExist:
			return self.cleaned_data['email']
		raise forms.ValidationError(
			_("Email already registered"),
			code = 'already_exists',
		)

	# clean_<fieldname> method in a form class is used to do custom validation for the field.
	# We are doing a custom validation for the 'password2' field and raising
	# a validation error if the password and its confirmation do not match
	# 
	# Read this link to know more about this method - https://docs.djangoproject.com/en/1.9/ref/forms/validation/#raising-validationerror
	def clean_password2(self):
		# cleaned_data dictionary has the valid fields
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError(
				_("Passwords do not match"),
				code = 'not_matching',
			)

		if len(password) < 6:
			raise forms.ValidationError(
				_("Password should be atleast 6 characters long"),
				code = 'too_short',
			)

		return password2


class LoginForm(forms.Form):
	email = forms.EmailField(label='Enter your email', widget=forms.EmailInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label='Enter your password')


class EditProfileForm(forms.Form):
	fname = forms.CharField(label='First name', max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	lname = forms.CharField(label='Last name', max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)

	gender = forms.ChoiceField(label='Gender', choices=GENDER_LIST, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	resume_url = forms.URLField(label='Resume URL', widget=forms.TextInput(attrs={'class' : 'form-control'}))

	summary = forms.CharField(label='Summary', widget=forms.TextInput(attrs={'class': 'form-control'}))

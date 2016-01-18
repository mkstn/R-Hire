#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-18 22:57:52
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-01-19 02:23:29

from django import forms


class RegistrationForm(forms.Form):
	fname = forms.CharField(label='First name', max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	lname = forms.CharField(label='Last name', max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)

	email = forms.EmailField(label='Enter your email', widget=forms.EmailInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), label='Enter your password')
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Should be same as password field, obviously'}), label='Confirm password')

	# clean_<fieldname> method in a form class is used to do custom validation for the field.
	# We are doing a custom validation for the 'password2' field and raising
	# a validation error if the password and its confirmation do not match
	def clean_password2(self):
		# cleaned_data dictionary has the valid fields
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError("Passwords do not match.")
		return password2

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-01-09 00:35:02


from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.

GENDER 	= (	('M', 'Male'),
			('F', 'Female'),
			('ND', 'Not Defined'))

class Candidate(Document):
	fname = StringField(verbose_name='First Name',max_length=200,required=True)
	lname = StringField(verbose_name='Last Name', max_length=200)
	photo_url = URLField(verbose_name='Photo URL', verify_exists=True)
	last_school = StringField(verbose_name='Last School Name', max_length=1000)
	email = EmailField(unique=True,required=True)
	password = StringField(max_length=500,required=True)
	summary = StringField()
	current_location = StringField(max_length=100)
	gender = StringField(max_length=2, choices=GENDER)
	resume_url = URLField(verify_exists=True)
	contact_number = StringField(max_length=10)
	address = StringField()
	dob = DateTimeField()

	def __str__(self):
		return self.fname

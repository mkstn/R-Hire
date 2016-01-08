#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-01-09 02:11:32


# from __future__ import unicode_literals

# from django.db import models

from mongoengine import *
import datetime

GENDER 	= (	('M', 'Male'),
			('F', 'Female'),
			('ND', 'Not Defined'))


WEBSITE_TYPE = ((1, 'unrecognized'),
				(2, 'Github'))


class Award(EmbeddedDocument):
	title = StringField(max_length=200, required=True)
	issuer = StringField(max_length=400)
	description = StringField()
	start_date = DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.title


class Course(EmbeddedDocument):
	title = StringField(max_length=100, required=True)
	authority = StringField(max_length=400)
	description = StringField()
	date = DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.title


class Education(EmbeddedDocument):
	school = StringField(max_length=200, required=True)
	degree = StringField(max_length=200, required=True)
	major = StringField(max_length=200)
	start_date = DateTimeField(default=datetime.datetime.now)
	end_date = DateTimeField(default=datetime.datetime.now)
	grade = StringField(max_length=20)
	description = StringField()

	def __str__(self):
		return self.degree


class Experience(EmbeddedDocument):
	company = StringField(max_length=200, required=True)
	position = StringField(max_length=200, required=True)
	start_date = DateTimeField(default=datetime.datetime.now)
	end_date = DateTimeField(default=datetime.datetime.now)
	description = StringField()

	def __str__(self):
		return self.company


class Project(EmbeddedDocument):
	title = StringField(max_length=200, required=True)
	description = StringField()
	url = URLField(verify_exists=True)
	end_date = DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.title


class Skill(EmbeddedDocument):
	title = StringField(max_length=200)

	def __str__(self):
		return self.title


class Website(EmbeddedDocument):
	url = URLField(verify_exists=True)
	website_type = IntField(max_length=2, choices=WEBSITE_TYPE)

	def __str__(self):
		return self.url


class Candidate(Document):
	fname = StringField(verbose_name='First Name',max_length=200,required=True)
	lname = StringField(verbose_name='Last Name', max_length=200)
	
	photo_url = URLField(verify_exists=True)
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

	awards = ListField(EmbeddedDocumentField('Award'))
	courses = ListField(EmbeddedDocumentField('Course'))
	educations = ListField(EmbeddedDocumentField('Education'))
	experiences = ListField(EmbeddedDocumentField('Experience'))
	projects = ListField(EmbeddedDocumentField('Project'))
	skills = ListField(EmbeddedDocumentField('Skill'))
	websites = ListField(EmbeddedDocumentField('Website'))

	def __str__(self):
		return self.fname


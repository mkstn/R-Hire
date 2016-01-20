#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-21 04:06:13


from __future__ import unicode_literals

from django.db import models


GENDER_LIST = (	('M', 'Male'),
				('F', 'Female'),
				('ND', 'Not Defined'),
				)


WEBSITE_TYPE = (('na', 'unrecognized'),
				('gh', 'Github'),
				('ln', 'LinkedIn'),
				('pw', 'Personal Website'),
				('tw', 'Twitter'),
				('fb', 'Facebook'),
				)


class Award(models.Model):
	title = models.CharField(max_length=200, blank=False)
	issuer = models.CharField(max_length=400)
	description = models.TextField(max_length=None)
	start_date = models.DateTimeField(default=None)
	candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
    )

	def __str__(self):
		return self.title


class Course(models.Model):
	title = models.CharField(max_length=100, blank=False)
	authority = models.CharField(max_length=400)
	description = models.TextField(max_length=None)
	date = models.DateTimeField(default=None)
	candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
    )

	def __str__(self):
		return self.title


class Education(models.Model):
	school = models.CharField(max_length=200, blank=False)
	degree = models.CharField(max_length=200, blank=False)
	major = models.CharField(max_length=200)
	start_date = models.DateTimeField(default=None)
	end_date = models.DateTimeField(default=None)
	grade = models.CharField(max_length=20)
	description = models.TextField(max_length=None)
	candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
    )

	def __str__(self):
		return self.degree


class Experience(models.Model):
	company = models.CharField(max_length=200, blank=False)
	position = models.CharField(max_length=200, blank=False)
	start_date = models.DateTimeField(default=None)
	end_date = models.DateTimeField(default=None)
	description = models.TextField(max_length=None)
	candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
    )

	def __str__(self):
		return self.company


class Project(models.Model):
	title = models.CharField(max_length=200, blank=False)
	description = models.TextField(max_length=None)
	url = models.URLField(default=None)
	end_date = models.DateTimeField(default=None)
	candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
    )

	def __str__(self):
		return self.title


class Skill(models.Model):
	title = models.CharField(max_length=200)
	candidate = models.ForeignKey(
		'Candidate',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.title


class Website(models.Model):
	url = models.URLField(default=None)
	website_type = models.CharField(max_length=3, choices=WEBSITE_TYPE)
	candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
    )

	def __str__(self):
		return self.url


class Candidate(models.Model):
	fname = models.CharField(verbose_name='First Name',max_length=200,blank=False)
	lname = models.CharField(verbose_name='Last Name', max_length=200,blank=True,null=True)
	
	photo_url = models.URLField(default=None,blank=True,null=True)
	last_school = models.CharField(verbose_name='Last School Name', max_length=1000,blank=True,null=True)
	
	email = models.EmailField(unique=True,blank=False)
	password = models.CharField(max_length=500,blank=False)
	
	summary = models.TextField(max_length=None,blank=True,null=True)
	current_location = models.CharField(max_length=100,blank=True,null=True)
	gender = models.CharField(max_length=2, choices=GENDER_LIST,blank=True,null=True)
	resume_url = models.URLField(default=None,blank=True,null=True)
	contact_number = models.CharField(max_length=10,blank=True,null=True)
	address = models.TextField(max_length=None,blank=True,null=True)
	dob = models.DateTimeField(default=None,blank=True,null=True)

	def __str__(self):
		return self.fname


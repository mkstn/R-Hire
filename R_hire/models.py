#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Sahil Dua
# @Date:   2016-01-08 22:48:10
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-01-19 02:38:10


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


# class Candidate(models.Model):
# 	fname = models.CharField(max_length=200, verbose_name="First name")
# 	lname = models.CharField(max_length=200, verbose_name="Last name")
# 	photo_url = models.CharField(max_length=500)
# 	last_school = models.CharField(max_length=1000)


# class CandidateLogin(models.Model):
# 	candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, verbose_name="related candidate", null=True, blank=True)
# 	email = models.CharField(max_length=500)
# 	password = models.CharField(max_length=500)
# 	created_tx = models.DateTimeField('Created at')

# 	class Meta:
# 		db_table = "R_hire_candidate_login"


# class CandidateDetails(models.Model):
# 	candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, verbose_name="related candidate", null=True, blank=True)
# 	summary = models.TextField()
# 	current_location = models.CharField(max_length=200)
# 	gender = models.CharField(max_length=1, default='M', choices = GENDER_LIST)
# 	resume_url = models.CharField(max_length=200)
# 	contact_number = models.CharField(max_length=20)
# 	address = models.TextField()
# 	dob = models.DateField()

# 	class Meta:
# 		db_table = "R_hire_candidate_details"


# class Awards(models.Model):
# 	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
# 	title = models.CharField(max_length=200)
# 	issuer = models.CharField(max_length=400)
# 	description = models.TextField()
# 	start_month = models.IntegerField()


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

	# awards = OneToMany(to=Award)
	# courses = OneToMany(to=Course)
	# educations = OneToMany(to=Education)
	# experiences = OneToMany(to=Experience)
	# projects = OneToMany(to=Project)
	# skills = OneToMany(to=Skill)
	# websites = OneToMany(to=Website)


	# courses = ListField(EmbeddedDocumentField('Course'))
	# educations = ListField(EmbeddedDocumentField('Education'))
	# experiences = ListField(EmbeddedDocumentField('Experience'))
	# projects = ListField(EmbeddedDocumentField('Project'))
	# skills = ListField(EmbeddedDocumentField('Skill'))
	# websites = ListField(EmbeddedDocumentField('Website'))

	def __str__(self):
		return self.fname


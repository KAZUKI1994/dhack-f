from django.db import models
from datetime import datetime
from django.utils import timezone
from django import forms
# Create your models here.

class Works(models.Model):
	IMADE = "IM"

	TANABE = "TN"
	CANPUS_CHOICE = (
		(IMADE , u'今出川'),
		(TANABE , u'京田辺'),
	)
	HIKEN = "Hi"
	Seikyo = "Se"
	PC = "Pc"
	Hozyo = "Ho"
	CATEGORY_CHOICE = (
		(HIKEN, u'被験者バイト'),
		(Seikyo, u'生協バイト'),
		(PC, u'PCバイト'),
		(Hozyo, u'補助バイト'),
	)
	
	title = models.CharField(max_length=30)
	publisher = models.CharField(max_length=20)
	pub_phone = models.IntegerField()
	pub_mail = models.EmailField(max_length=254)
	content = models.TextField()
	condition = models.CharField(max_length=100)
	canpus = models.CharField(max_length=2, choices=CANPUS_CHOICE)
	location = models.CharField(max_length=100)
	work_period = models.DateField()
	dead_line = models.DateField()
	can_time = models.DateField()
	pay = models.CharField(max_length=20)
	category = models.CharField(max_length=2, choices=CATEGORY_CHOICE)
	
	#top_image = models.FilePathField(upload_to=None, max_length=100)


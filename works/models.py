from django.db import models

# Create your models here.

class Works(models.Model):
	CANVAS_CHOICE = (
		('IM' , u'今出川'),
		('TN' , u'京田辺'),
	)
	title = models.CharField(max_length=30)
	publisher = models.CharField(max_length=20)
	pub_phone = models.IntegerField()
	pub_mail = models.EmailField(max_length=254)
	content = models.TextField()
	condition = models.CharField(max_length=100)
	canvas = models.CharField(max_length=2, choices=CANVAS_CHOICE)
	location = models.CharField(max_length=100)
	work_start = models.DateField()
	work_finish = models.DateField()
	money_kind = models.CharField(max_length=20)
	money_amount = models.IntegerField()
	#top_image = models.FilePathField(upload_to=None, max_length=100)


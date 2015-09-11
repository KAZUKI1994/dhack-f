from django.db import models
from datetime import datetime
from django.utils import timezone
from django.forms.models import BaseModelFormSet
from django.forms import ModelForm


# Create your models here.

class Works(models.Model):

	CANPUS_CHOICE = (
		(0 , u'今出川'),
		(1 , u'京田辺'),
	)
	
	CATEGORY_CHOICE = (
		(0, u'被験者バイト'),
		(1, u'生協バイト'),
		(2, u'PCバイト'),
		(3, u'授業補助'),
		(4, u"イベント"),
	)
	
	title = models.CharField(max_length=30)
	category = models.IntegerField(choices=CATEGORY_CHOICE)
	publisher = models.CharField(max_length=20)
	pub_phone = models.IntegerField()
	pub_mail = models.EmailField(max_length=254)
	content = models.TextField()
	condition = models.CharField(max_length=100)
	canpus = models.IntegerField(choices=CANPUS_CHOICE)
	location = models.CharField(max_length=100)
	work_period = models.CharField(max_length=300)
	dead_line = models.DateField()
	pay = models.CharField(max_length=20)
	
	#top_image = models.FilePathField(upload_to=None, max_length=100)
class WorksForm(ModelForm):
	class Meta:
		model = Works
		fields = "__all__"

class BaseWorksFormSet(BaseModelFormSet):
	def __init__(self, *args, **kwargs):
		super(BaseWorksFormSet, self).__init__(*args, **kwargs)
		self.queryset = Works.objects.filter(name__startswith='O')


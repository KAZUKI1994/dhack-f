from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
#from django.template import RequestContext, loader

from .models import Works

# Create your views here.
#トップ画面
class IndexView(generic.ListView):
	template_name="works/index.html"
	context_object_name="new_archieve_list"

	def get_queryset(self):
		return Works.objects.order_by('work_start')[:10]

#バイト詳細情報画面
class DetailView(generic.DetailView):
	model = Works
	template_name = "works/detail.html"

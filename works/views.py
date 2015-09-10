from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.template import RequestContext, loader

from .models import Works
from .forms import NameForm

# Create your views here.
#トップ画面
class IndexView(generic.ListView):
	template_name="works/index.html"
	#get_template_names="base.html"
	context_object_name="new_archieve_list"
	#############


	def get_queryset(self):
		return Works.objects.order_by('dead_line')[:10]

#バイト詳細情報画面
class DetailView(generic.DetailView):
	#model = Works
	template_name = "works/detail.html"


#ユーザー情報
def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = NameForm()

	return render(request, 'name.html', {'form' : form})


#バイトフォーム画面
#class jobform(View):

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
<<<<<<< HEAD
from django.views import generic
#from django.template import RequestContext, loader
from works.forms import UserForm
=======
from django.views import generic, View
from django.template import RequestContext, loader
>>>>>>> 3ec9592f67b81d75750884e63848e05e350d1087

from .models import Works
from .forms import UserForm

# Create your views here.
#トップ画面
class IndexView(generic.TemplateView):
	template_name="works/index.html"
	#get_template_names="base.html"
	context_object_name="new_archieve_list"
	#############


	def get_queryset(self):
		return Works.objects.order_by('work_start')[:10]

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
<<<<<<< HEAD
#class job_form(TemplateView):#generic.DetailView):
template_name = "works/jobform.html"

def job_form(request):
    form = Works()
    return render(request, template_name, {'form': form})
=======
#class jobform(View):
>>>>>>> 3ec9592f67b81d75750884e63848e05e350d1087

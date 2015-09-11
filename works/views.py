from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.template import RequestContext, loader
<<<<<<< HEAD
=======

>>>>>>> 54a0fd93c59901ae7dde160a2ca48d9acc726769
from django.templatetags.static import static
from django.views.generic.edit import FormView
from django.forms.models import modelformset_factory
from .models import Works, WorksForm
from .forms import ContactForm
<<<<<<< HEAD
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from .models import Works
from .forms import UserForm

=======

from .models import Works
from .forms import UserForm
>>>>>>> 54a0fd93c59901ae7dde160a2ca48d9acc726769

# Create your views here.
#トップ画面
class IndexView(generic.ListView):
	template_name="works/index.html"
	#get_template_names="base.html"
	context_object_name="new_archieve_list"
	#############

	icon_images = {
		0 : static("images/img0.png"),
		1 : static("images/img1.png"),
		2 : static("images/img2.png"),
		3 : static("images/img3.png"),
		4 : static("images/img4.png"),
	}



	def get_queryset(self):
		return Works.objects.order_by('dead_line')[:10]

#バイト詳細情報画面
class DetailView(generic.DetailView):
	#model = Works
	template_name = "works/detail.html"



#バイトフォーム画面
@csrf_protect
def jobform(request):
	JobFormSet = modelformset_factory(Works, fields="__all__")
	if request.method == "POST":
		formset = JobFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = JobFormSet()
	ctxt = RequestContext(request, {})
	return render_to_response("works/jobform.html", {"formset":formset}, ctxt)

#カテゴリー別一覧画面


#コンタクトフォーム
class ContactView(FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = '/thanks/'

<<<<<<< HEAD
=======

>>>>>>> 54a0fd93c59901ae7dde160a2ca48d9acc726769
	def form_valid(self, form):
		form.send_email()
		return super(ContactView, self).form_valid(form)

#バイトフォーム画面
#class jobform(View):

def userform(request):
    form = UserForm()

    return render(request,'works/jobform.html',{'form':form})
<<<<<<< HEAD
=======

>>>>>>> 54a0fd93c59901ae7dde160a2ca48d9acc726769

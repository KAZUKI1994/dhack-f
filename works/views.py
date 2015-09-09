from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
#from django.template import RequestContext, loader

from .models import Works

# Create your views here.

#top画面
def index(request):
	new_archieve_list = Works.objects.order_by('work_start')[:10]
	context = {'new_archieve_list' : new_archieve_list}
	return render(request, 'works/index.html', context)
	#template = loader.get_template('works/index.html')
	#context = RequestContext(request, {
	#	'new_archieve_list' : new_archieve_list,
	#	})
	#output = ', '.join([p.title for p in new_archieve_list])
	return HttpResponse(template.render(context))

def detail(request, works_id):
	work = get_object_or_404(Works, pk=works_id)
	return render(request, 'works/detail.html', {'work': work})
	
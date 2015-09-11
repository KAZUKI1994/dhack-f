from django.conf.urls import url, patterns
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^jobform/$', views.jobform ,name="jobform"),
<<<<<<< HEAD
	url(r'^contact/$', views.FormView.as_view(), name='contact'),
	url(r'^form/',views.userform,name="jobform")
] 
  
=======
    url(r'^contact/$', views.FormView.as_view(), name='contact'),
    url(r'^form/',views.userform,name="jobform"),
] 
>>>>>>> 6c6fce1b1b2035a3e38a0bd4dd5c52a72e861683

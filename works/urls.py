from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
        url(r'^form/',views.job_form,),
=======
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
#    url(r'^form/',views.form,name="jobform")
>>>>>>> 3ec9592f67b81d75750884e63848e05e350d1087
]

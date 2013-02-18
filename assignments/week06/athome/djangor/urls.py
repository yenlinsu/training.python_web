from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from djangor.models import BlogPost
from djangor.views import BlogEntryList

def stub(request, *args, **kwargs):
    return HttpResponse('stub view', mimetype="text/plain")

urlpatterns = patterns('',
    url(r'^$', BlogEntryList.as_view(), name="entry_list"),
    url(r'^(?P<pk>\d+)/$', 'djangor.views.entry_detail', name="entry_detail"),
    url(r'^new/$', stub,
    #    DetailView.as_view(
    #        model=BlogPost,
    #        template_name="blogs/detail.html"),
        name="entry_new"),
    #url(r'^(?P<pk>\d+)//$', stub,
    #    #'polls.views.vote_view',
    #    name="poll_vote"),
    #url(r'^(?P<pk>\d+)//$', stub,
    #    #DetailView.as_view(
    #    #    model=Poll,
    #    #    template_name="blogs/result.html"),
    #    name="poll_result"),
)

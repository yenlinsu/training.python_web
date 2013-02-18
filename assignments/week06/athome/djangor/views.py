from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from djangor.models import BlogPost
from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response

class BlogEntryList(ListView):
    model = BlogPost
    template_name = "blogs/list.html"
    context_object_name = 'blog_entries'

def entry_detail(*args, **kwargs):
    for arg in kwargs:
        pk = kwargs[arg]
    entry = BlogPost.objects.get(pk=pk)
    return render_to_response('blogs/detail.html', {'title': entry.title, 'body': entry.body, 'date': entry.pub_date})

"""
def vote_view(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == "POST":
        try:
            choice = poll.choice_set.get(
                pk=request.POST.get('choice', 0))
        except Choice.DoesNotExist:
            msg = "Ooops, pick a choice that exists, please"
            messages.add_message(request, messages.ERROR, msg)
            url = reverse('poll_detail', args=[pk, ])
        else: # vote and send to result
            choice.votes += 1
            choice.save()
            messages.add_message(request, messages.INFO,
                             "You voted for %s" % choice)
            url = reverse('poll_result', args=[pk])
    else: # submitted via GET, ignore it
        url = reverse('poll_detail', args=[pk, ])

    return HttpResponseRedirect(url)
"""
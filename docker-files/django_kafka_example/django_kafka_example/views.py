from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateTopicForm

def create_topic(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateTopicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateTopicForm()

    return render(request, 'create-topic.html', {'form': form})

def get_topics(request):
    
    return render(request, 'get-topics.html', {'title': 'new title', 'cal': 'new cal'} )
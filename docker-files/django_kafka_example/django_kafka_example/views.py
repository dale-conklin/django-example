from django.http import HttpResponseRedirect
from django.http import HttpResponse    
from django.shortcuts import render

from .forms import CreateTopicForm, CreateEventForm, GetEventsForm
from .kafka_actions import get_kafka_topics, create_kafka_topic, produce_kafka_event, get_kafka_events

def create_topic(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateTopicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(f"{form.cleaned_data}")
            create_kafka_topic(form.cleaned_data.get('topic_name'))
            # redirect to a new URL:
            return HttpResponseRedirect('/get-topics/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateTopicForm()

    return render(request, 'create-topic.html', {'form': form})

def get_topics(request):
    topics = get_kafka_topics()
    #return render(request, 'get-topics.html', {'title': 'new title', 'cal': 'new cal'} )
    return HttpResponse(f"{topics}")

def create_event(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateEventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            produce_kafka_event(form.cleaned_data.get('topic_name'), form.cleaned_data.get('event_str'))
            # redirect to a new URL:
            return HttpResponseRedirect('/get-events/')
    else:
        form = CreateEventForm()

    return render(request, 'create-event.html', {'form': form})

def get_events(request):
    events = []
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetEventsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            events = get_kafka_events(form.cleaned_data.get('topic_name'))
    else:
        form = GetEventsForm()
    # html = ''.join(str(f'<br>{e}<br>') for e in events)

    return render(request, 'get-events.html', {'form': form, 'events': events})
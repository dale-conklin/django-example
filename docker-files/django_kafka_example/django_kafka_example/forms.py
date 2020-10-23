from django import forms
from . import kafka_actions

class CreateTopicForm(forms.Form):
    topic_name = forms.CharField(label='New Topic', max_length=100)


class CreateEventForm(forms.Form):
    choices = []
    topics = kafka_actions.get_kafka_topics()
    for topic in topics:
        choices.append(tuple((topic, topic)))
    topic_name = forms.CharField(label='Topic: ', widget=forms.Select(choices=choices))
    event_str = forms.CharField(label='Event', max_length=250)


class GetEventsForm(forms.Form):
    choices = [('','')]
    topics = kafka_actions.get_kafka_topics()
    for topic in topics:
        choices.append(tuple((topic, topic)))
    topic_name = forms.CharField(label='Topic: ', widget=forms.Select(choices=choices))

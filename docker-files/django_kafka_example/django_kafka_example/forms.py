from django import forms

class CreateTopicForm(forms.Form):
    topic_name = forms.CharField(label='New Topic', max_length=100)


class CreateEventForm(forms.Form):
    topic_name = forms.CharField(label='Topic', max_length=100)
    event_str = forms.CharField(label='Event', max_length=250)
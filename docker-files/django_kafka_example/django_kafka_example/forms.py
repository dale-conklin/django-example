from django import forms

class CreateTopicForm(forms.Form):
    topic_name = forms.CharField(label='New Topic', max_length=100)
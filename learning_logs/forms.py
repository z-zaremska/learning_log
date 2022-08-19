from socket import fromshare
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        #kolumny
        fields = ['text']
        #etykiety
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        lables = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

from django import forms
from .models import Chapter,Entry,Exercise

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': '章节名称'}
        
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['topic','text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100,'rows': 10})}
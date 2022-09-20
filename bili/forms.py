
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
        labels = {'topic': '习题名称','text':'习题内容'}
        widgets = {'text': forms.Textarea(attrs={'class': "form-control",
'style': 'width: 75%','rows': 22}),
                  'topic': forms.TextInput(attrs={'class': "form-control",
'style': 'width: 75%'})}
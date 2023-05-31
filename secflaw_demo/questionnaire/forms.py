from django import forms
from .models import Answer

class QuestionForm(forms.Form):
    class Meta:
        model = Answer
        fields = ['answer']
        labels = {'answer': 'Answer'}
    answer = forms.CharField(required=True)


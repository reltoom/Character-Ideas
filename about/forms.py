from django import forms
from .models import QuestionForUs



class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionForUs
        fields = ('name', 'email', 'message')
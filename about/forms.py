from .models import QuestionForUs
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionForUs
        fields = ('name', 'email', 'message')
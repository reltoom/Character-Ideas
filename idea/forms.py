from django import forms
from django.utils.text import slugify
from .models import Comment, Character



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['title', 'content',]

    title = forms.CharField(max_length=100, required=True)
    content = forms.TextInput()

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(self.cleaned_data['title'])
        if commit:
            instance.save()
        return instance
        
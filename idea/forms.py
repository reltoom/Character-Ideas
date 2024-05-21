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
        fields = ['title', 'content', 'featured_image']

    title = forms.CharField(max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea)


    def clean_title(self):
        title = self.cleaned_data['title']
        # Check if a character with the same title exists
        if Character.objects.filter(title__iexact=title).exists():
            raise forms.ValidationError("A character with this title already exists.")
        return title

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(self.cleaned_data['title'])
        if commit:
            instance.save()
        return instance
        
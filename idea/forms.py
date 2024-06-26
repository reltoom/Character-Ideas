from django import forms
from django.utils.text import slugify
from .models import Comment, Character
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['title',
                  'race',
                  'gender',
                  'class_archetype',
                  'weapons',
                  'armor',
                  'character_picture',
                  'description',
                  'excerpt', ]

    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea)
    excerpt = forms.CharField(max_length=200, required=False)
    weapons = forms.CharField(max_length=100, required=False)
    armor = forms.CharField(max_length=100, required=False)
    character_picture = CloudinaryFileField(required=False)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        instance = self.instance
        if instance.title != title:
            # Title has been changed,
            # check if a character with the new title exists
            if Character.objects.filter(title__iexact=title).exists():
                raise forms.ValidationError(
                    "A character with this title already exists.")
        return title

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(self.cleaned_data['title'])
        if commit:
            instance.save()
        return instance

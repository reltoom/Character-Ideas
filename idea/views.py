from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.forms.utils import ErrorList
from .models import Character, Comment
from .forms import CommentForm, CharacterForm

# Create your views here.
class CharacterList(generic.ListView):
    queryset = Character.objects.filter(status=1)
    template_name = "idea/index.html"
    paginate_by = 4


def character_detail(request, slug):
    """
    Display an individual :model:`idea.Character`.

    **Context**

    ``character``
        An instance of :model:`idea.Character`.

    **Template:**

    :template:`idea/character_detail.html`
    """

    queryset = Character.objects.filter(status=1)
    character = get_object_or_404(queryset, slug=slug)
    comments = character.comments.all().order_by("-created_on")
    comment_count = character.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.creator = request.user
            comment.character = character
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment created!')
            
    comment_form = CommentForm()

    return render(
        request,
        "idea/character_detail.html",
        {"character": character,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,},
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Character.objects.filter(status=1)
        character = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.creator == request.user:
            comment = comment_form.save(commit=False)
            comment.character = character
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('character_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Character.objects.filter(status=1) 
    character = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.creator == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('character_detail', args=[slug]))


@login_required
def create_character(request):
    if request.method == 'POST':
        character_form = CharacterForm(request.POST, request.FILES)
        if character_form.is_valid():
            character = character_form.save(commit=False)
            character.creator = request.user
            character.save()
            return redirect('home')  # Redirect to the 'home' after save
        else:
             # Check if the error is due to non-unique title
            if 'title' in character_form.errors:
                # Pre-fill the form with user entered data
                character_form = CharacterForm(request.POST)
                # Error message displays to the form
                character_form.errors['title'] = ErrorList([
                    "A character with this title already exists."])
                # Render the form with errors
                return render(request, 'idea/create_character.html',
                              {'character_form': character_form})
    
    # GET request - display the empty form
    character_form = CharacterForm()
    return render(request, 'idea/create_character.html', {'character_form': character_form})


@login_required
def my_characters(request):
    """
    Display a list of characters created by the logged-in user.
    """
    characters = Character.objects.filter(creator=request.user)
    return render(request, 'idea/my_characters.html', {'characters': characters})


class MyCharactersList(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'idea/my_characters.html'
    context_object_name = 'characters'
    paginate_by = 4

    def get_queryset(self):
        return Character.objects.filter(creator=self.request.user)
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Character, Comment
from .forms import CommentForm

# Create your views here.
class CharacterList(generic.ListView):
    queryset = Character.objects.filter(status=1)
    template_name = "idea/index.html"
    paginate_by = 2


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
                'Comment submitted and awaiting approval')
            
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
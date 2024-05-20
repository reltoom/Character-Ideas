from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Character
from .forms import CommentForm
from django.contrib import messages

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
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Character

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

    return render(
        request,
        "idea/character_detail.html",
        {"character": character,
         "comments": comments,
         "comment_count": comment_count,},
    )
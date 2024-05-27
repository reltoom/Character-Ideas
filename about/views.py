from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import QuestionForm


def about(request):
    if request.method == "POST":
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            question_form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "Thanks for contacting Character Share"
                                 " with your inquiry!"
                                 "We will get back to you soon!")

    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    question_form = QuestionForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "question_form": question_form},
    )

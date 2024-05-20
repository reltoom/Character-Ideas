from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class QuestionForUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    answered = models.BooleanField(default=False)

    def __str__(self):
        return f"A question from {self.name}"
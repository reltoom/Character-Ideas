from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Character(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    creator = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="idea_characters"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    excerpt = models.TextField(blank=True, max_length=200)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on", "creator"]
    
    def __str__(self):
        return f"{self.title} | by {self.creator}"


class Comment(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="comments")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} |  {self.creator}"
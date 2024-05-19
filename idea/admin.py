from django.contrib import admin
from .models import Character, Comment

# Register models here.
admin.site.register(Character)
admin.site.register(Comment)
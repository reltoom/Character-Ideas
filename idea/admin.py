from django.contrib import admin
from .models import Character, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Character) 
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register models here.
admin.site.register(Comment)
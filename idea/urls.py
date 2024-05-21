from django.urls import path
from . import views


urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path('create/', views.create_character, name='create_character'),
    path('my_characters/', views.my_characters, name='my_characters'),
    path('<slug:slug>/', views.character_detail, name='character_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
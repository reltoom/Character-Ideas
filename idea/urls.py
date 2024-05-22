from django.urls import path
from . import views


urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path('create/', views.create_character, name='create_character'),
    path('my_characters/', views.MyCharactersList.as_view(), name='my_characters'),
    path('<slug:slug>/', views.character_detail, name='character_detail'),
    path('<slug:slug>/edit/', views.edit_character, name='edit_character'),
    path('<slug:slug>/delete/', views.delete_character, name='delete_character'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
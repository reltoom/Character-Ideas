from . import views
from django.urls import path

urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path('<slug:slug>/', views.character_detail, name='character_detail'),
]
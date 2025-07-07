from django.urls import path
from . import views

urlpatterns = [
    path('chat-messages/', views.ChatMessageListCreateView.as_view(), name='chat-message-list'),
]
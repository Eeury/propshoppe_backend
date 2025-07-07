from django.shortcuts import render

from rest_framework import generics
from .models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user.email if self.request.user.is_authenticated else 'Anonymous')
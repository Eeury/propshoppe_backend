from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    class Meta:
        model = ChatMessage
        fields = ['user', 'message', 'timestamp', 'is_admin_response']
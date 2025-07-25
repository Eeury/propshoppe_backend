from django.db import models

from django.db import models

class ChatMessage(models.Model):
    user = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_admin_response = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user}: {self.message}"

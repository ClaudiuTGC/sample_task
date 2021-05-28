from rest_framework import serializers
from .models import *

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('__all__')

class ChatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chat
		fields = ('__all__')
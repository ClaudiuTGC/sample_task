from rest_framework import serializers

from .models import *

class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversation
        fields = ('__all__')

class ChatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Chat
		fields = ('__all__')
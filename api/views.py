from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import *
from .models import *


class ConversationApiView(APIView):
	
	def get(self, request, id):
		conversations = Conversation.objects.filter(id=id)
		chat = Chat.objects.filter(conversationId=id)
		serializer_conversation = ConversationSerializer(conversations, context={'request': request}, many=True)
		serializer_chat = ChatSerializer(chat, context={'request': request}, many=True)
		return Response(serializer_conversation.data + serializer_chat.data, status=status.HTTP_200_OK)

class ChatApiView(APIView):
	def get(self, request, id):
		chats = Chat.objects.filter(id=id)
		serializer = ChatSerializer(chats, context={'request': request}, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = ChatSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		




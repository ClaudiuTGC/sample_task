from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import *
from .models import *


class ConversationApiView(APIView):
	
	def get(self, request, id, *args, **kwargs):
		conversations = Conversation.objects.filter(id=id)
		serializer = ConversationSerializer(conversations, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class ChatApiView(APIView):
	def get(self, request, id, *args, **kwargs):
		chats = Chat.objects.filter(id=id)
		serializer = ChatSerializer(chats, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		data = {
			'payload': request.data.get('payload'),
			'userId': request.user.id
		}
		serializer = ChatSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		




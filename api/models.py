from django.db import models
from django.contrib.auth.models import User 

class Chat(models.Model):
	conversationId = models.ForeignKey('Conversation', on_delete=models.SET_NULL, null=True)
	payload  = models.CharField(max_length=300, null=False) 
	userId   = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
	utc_date = models.DateTimeField(auto_now_add=True)
	status   = models.CharField(max_length=50, default="new")

class Operator(models.Model):
	group = models.CharField(unique=True, max_length=100)
	name  = models.CharField(max_length=100)

class Client(models.Model):
	pass

class ScheduleTable(models.Model):
	pass

class Store(models.Model):
	name = models.CharField(max_length=100)
	discountCode = models.CharField(max_length=100)

class Conversation(models.Model):
	storeId       = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
	operatorId    = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True, related_name='operatorId')
	clientId      = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
	operatorGroup = models.ForeignKey(Operator, to_field='group', on_delete=models.SET_NULL, null=True, related_name='operatorGroup')


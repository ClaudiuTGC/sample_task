from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('conversation/<int:id>/', ConversationApiView.as_view()),
    path('chat/<int:id>/', ChatApiView.as_view()),
]
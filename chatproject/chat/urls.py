from django.urls import path
from .views import MessageListView, MessageCreateView

urlpatterns = [
    path('messages/<int:chatroom_id>/', MessageListView.as_view(), name='message-list'),
    path('messages/<int:chatroom_id>/send/', MessageCreateView.as_view(), name='message-create'),

]

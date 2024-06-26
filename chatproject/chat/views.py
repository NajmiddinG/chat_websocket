from rest_framework import generics
from .models import Message, ChatRoom
from .serializers import MessageSerializer

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        chatroom_id = self.kwargs['chatroom_id']
        return Message.objects.filter(chatroom_id=chatroom_id).order_by('timestamp')


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        chatroom_id = self.kwargs['chatroom_id']
        serializer.save(chatroom_id=chatroom_id)
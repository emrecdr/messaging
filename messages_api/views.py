from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Message
from .serializers import MessageSerializer


class MessageListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all messages for given requested user
        '''
        payload = Message.objects.filter(receiver = request.user.id)
        serializer = MessageSerializer(payload, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        '''
        Create new message
        '''
        data = {
            'message': request.data.get('message'), 
            'sender': request.user.id,
            'receiver': request.data.get('receiver_id'),
        }
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

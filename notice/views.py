import notice
from django.contrib.auth.models import User
from notice.serializers import CreateNoticeSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class NoticesCreated(viewsets.ModelViewSet):
    '''
    Create new notices
    '''
    queryset = User.objects.all()
    serializer_class = CreateNoticeSerializer
    # def post(self, request, format=None):
    #     serializer = CreateNoticeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

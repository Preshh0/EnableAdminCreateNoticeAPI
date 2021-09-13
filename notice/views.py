import notice, requests
from django.http import JsonResponse
from notice.serializers import CreateNoticeSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status


class NoticesCreated(views.APIView):
    '''
    Create new notices
    '''
    def post(self, request):
        serializer = CreateNoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

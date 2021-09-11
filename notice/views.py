import notice
from notice.models import CreateNotice
from notice.serializers import CreateNoticeSerializer
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class NoticesCreated(APIView):
    '''
    Lists all notices/create new notices
    '''
    def get(self, request, format=None):
        notice = CreateNotice.objects.all()
        serializer = CreateNoticeSerializer(notice, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CreateNoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoticesDetail(APIView):
    """
    Retrieve, update or delete a code snippet
    """
    def get_object(self,pk):
        try:
            return CreateNotice.objects.get(pk=pk)
        except CreateNotice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        notice = self.get_object(pk)
        serializer = CreateNoticeSerializer(notice)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        notice = self.get_object(pk)
        serializer = CreateNoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        notice = self.get_object(pk)
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
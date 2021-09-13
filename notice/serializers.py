from rest_framework import serializers


class CreateNoticeSerializer(serializers.Serializer):

    username = serializers.CharField(max_length = 20)
    title = serializers.CharField(max_length = 20)
    department = serializers.CharField(max_length = 20)
    announcement = serializers.CharField(max_length = 20)
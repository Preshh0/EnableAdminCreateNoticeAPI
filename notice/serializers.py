from rest_framework import serializers
from notice.models import CreateNotice


class CreateNoticeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreateNotice
        fields = [
            'id', 'author', 'title', 'department', 'announcement'
        ]
    # id = serializers.IntegerField(read_only=True)
    # author = serializers.CharField(max_length=20)
    # title = serializers.CharField(max_length=30)
    # department = serializers.CharField(max_length=30)
    # announcement = serializers.CharField(max_length=200)

    # def create(self, validated_data):
    #     '''
    #     Create and return a new notice
    #     '''
    #     return CreateNotice.objects.create(**validated_data)
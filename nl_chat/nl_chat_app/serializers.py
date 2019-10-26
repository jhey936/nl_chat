from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Message

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    recieved_time = serializers.DateTimeField(required=True, allow_blank=False)
    sender = serializers.CharField(required=True, allow_blank=False)
    content = serializers.CharField(allow_blank=True, required=True)
    reply_sent = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


    # sender = models.TextField()
    # content = models.TextField()
    # reply_sent = models.BooleanField(default=False)

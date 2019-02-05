from rest_framework import serializers
from events.models import Event
from django.contrib.auth.models import User
from events.serializers.event import EventSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'events')

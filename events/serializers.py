from rest_framework import serializers
from events.models import Event
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'events')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'id', 'title', 'presenter', 'time', 'location', 'coordinator', 'description')

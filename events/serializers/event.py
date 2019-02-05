from rest_framework import serializers
from events.models import Event
from django.contrib.auth.models import User
from events.serializers.user import UserSerializer


class EventSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        'coordinator': UserSerializer,
    }
    class Meta:
        model = Event
        fields = ('url', 'id', 'title', 'presenter', 'time', 'location', 'coordinator', 'description')

    class JSONAPIMeta:
        included_resources = ['coordinator']


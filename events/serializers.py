from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=256)
    presenter = serializers.CharField(required=False, allow_blank=True, max_length=256)
    time = serializers.DateTimeField()
    location = serializers.CharField(required=False, allow_blank=True, max_length=256)
    coordinator = serializers.CharField(required=False, allow_blank=True, max_length=256)
    description = serializers.CharField(required=False, allow_blank=True, max_length=256)

    def create(self, validated_data):
        """
        Create and return a new `Event` instance, given the validated data.
        """
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.presenter = validated_data.get('presenter', instance.presenter)
        instance.time = validated_data.get('time', instance.time)
        instance.location = validated_data.get('location', instance.location)
        instance.coordinator = validated_data.get('coordinator', instance.coordinator)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

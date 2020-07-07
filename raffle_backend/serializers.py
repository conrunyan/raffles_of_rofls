from raffle_backend.models import Participant, Session, Winner, Host
from rest_framework import serializers


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ['name', 'ip_address', 'session']

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'host_token', 'session']


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['session_id', 'started_time']

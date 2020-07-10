from raffle_backend.models import Participant, Session, Winner, Host
from rest_framework import serializers


class ParticipantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    ip_address = serializers.IPAddressField()
    session_id = serializers.CharField(max_length=50)



class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'host_token']


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['session_id', 'started_time', 'host_id']

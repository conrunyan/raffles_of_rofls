from raffle_backend.models import Participant, Session, Winner, Host
from rest_framework import viewsets
from raffle_backend.serializers import ParticipantSerializer, HostSerializer


class ParticipantViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class HostViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer

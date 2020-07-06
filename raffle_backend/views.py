from raffle_backend.models import Participant, Session, Winner, Host
from rest_framework import viewsets
from raffle_backend.serializers import ParticipantSerializer, HostSerializer


class ParticipantViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class HostViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = HostSerializer

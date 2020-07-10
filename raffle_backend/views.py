import logging

from raffle_backend.models import Participant, Session, Winner, Host
from rest_framework import viewsets, status
from rest_framework.response import Response
from raffle_backend.serializers import ParticipantSerializer, HostSerializer, SessionSerializer

logger = logging.getLogger(__name__)


class ParticipantViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows Participants to be viewed or added
    """
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                session = Session.objects.get(
                    session_id=request.data['session_id'])
                Participant.objects.create(
                    name=request.data['name'],
                    ip_address=request.data['ip_address'],
                    session=session)
                return Response({'status': f"New user {request.data['name']} successfully added to session {request.data['session_id']}"})
            except Session.DoesNotExist:
                logger.warning(
                    f"Session {request.data['session_id']} does not exist")
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, pk=None):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class HostViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class SessionViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

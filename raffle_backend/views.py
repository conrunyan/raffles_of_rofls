from raffle_backend.models import Participant, Session, Winner, Host
from rest_framework import viewsets
from raffle_backend.serializers import ParticipantSerializer, HostSerializer, SessionSerializer


class ParticipantViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()

    def create(self, request, pk=None):
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            try:
                pass
                Session.objects.get()
            except:
                pass
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


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

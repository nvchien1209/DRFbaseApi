from rest_framework import generics
from .models import Note
from .serializer import NoteSerializer

class Notelist(generics.ListCreateAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer


class NoteDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset=Note.objects.all()
    serializer_class=NoteSerializer

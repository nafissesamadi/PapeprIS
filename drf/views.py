from django.shortcuts import render

from .serializers import PaperSerializer,AuthorSerializer
from rest_framework import generics, mixins
from paper.models import Paper,Author

# Create your views here.
#region generics for Paper
class PaperApiView(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

class PaperDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Paper.objects.all()
    serializer_class = PaperSerializer
#endregion

#region generics for Paper
class AuthorApiView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class = AuthorSerializer
#endregion




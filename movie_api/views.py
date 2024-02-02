# views.py in your movies app
from rest_framework import viewsets
from .models import MovieData
from .serializers import MovieDataSerializer
from rest_framework.filters import SearchFilter

class MovieDataViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer
    filter_backends = [SearchFilter]
    search_fields = ('title','description','year')

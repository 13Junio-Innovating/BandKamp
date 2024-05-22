from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Album
from .serializers import AlbumSerializer

class AlbumView(ListCreateAPIView):
    authentication_classes= [JWTAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AlbumDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs['pk'])
        serializer = self.get_serializer(album)
        return Response(serializer.data)

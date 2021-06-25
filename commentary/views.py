from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from commentary import serializers
from commentary.models import Commentary
from commentary.permissions import IsOwnerOrReadOnly


class CommentaryListCreateView(generics.ListCreateAPIView):
    queryset = Commentary.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('post',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentary.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CommentaryDeleteView(generics.DestroyAPIView):
    queryset = Commentary.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
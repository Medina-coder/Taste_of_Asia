from rest_framework import generics
from category import serializers
from category.models import Category
from django_filters import rest_framework as filters


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FoodDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

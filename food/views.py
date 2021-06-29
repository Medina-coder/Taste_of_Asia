from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from commentary.permissions import IsOwnerOrReadOnly
from food import serializers
# from food.management.commands.parser import main
from food.models import Food, Like, Basket, Favorites, Foods
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.select_related('owner', 'category', 'category__parent')
    serializer_class = serializers.FoodSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('price', 'quantity', 'title',)
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(id__icontains=search) | Q(price__icontains=search))
        return queryset

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response


class FoodCreateView(generics.CreateAPIView):
    serializer_class = serializers.FoodSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FoodDeleteView(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = serializers.FoodSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class FoodDetailView(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = serializers.FoodSerializer


class FoodUpdateView(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = serializers.FoodSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class BasketListView(generics.ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = serializers.BasketSerializer


class BasketCreateView(generics.CreateAPIView):
    serializer_class = serializers.BasketSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BasketDeleteView(generics.DestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = serializers.BasketSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer


class LikeCreateView(generics.CreateAPIView):
    serializer_class = serializers.LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class FavoritesListView(generics.ListAPIView):
    queryset = Favorites.objects.all()
    serializer_class = serializers.FavoritesSerializer


class FavoritesCreateView(generics.CreateAPIView):
    serializer_class = serializers.FavoritesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoritesDeleteView(generics.DestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = serializers.FavoritesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ParserListView(generics.ListAPIView):
    queryset = Foods.objects.all()
    serializer_class = serializers.FoodsSerializers

#
# @api_view(['POST'])
# def ParsingCreateView(request):
#     main()
#     return Response("Parsing is successfully done", status=status.HTTP_201_CREATED)



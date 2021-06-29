from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.FoodCreateView.as_view()),
    path('', views.FoodListView.as_view()),
    path('<int:pk>/', views.FoodDetailView.as_view()),
    path('update/<int:pk>/', views.FoodUpdateView.as_view()),
    path('<int:pk>/delete/', views.FoodDeleteView.as_view()),
    path('basket/<int:pk>/delete/', views.BasketDeleteView.as_view()),
    path('basket/', views.BasketListView.as_view()),
    path('basket/create/', views.BasketCreateView.as_view()),
    path('like/', views.LikeListView.as_view()),
    path('like/create/', views.LikeCreateView.as_view()),
    path('like/<int:pk>/delete/', views.LikeDeleteView.as_view()),
    path('favorites/', views.FavoritesListView.as_view()),
    path('favorites/create/', views.FavoritesCreateView.as_view()),
    path('favorites/<int:pk>/delete/', views.FavoritesDeleteView.as_view()),
    path('foods/', views.ParserListView.as_view()),
    # path('parsing/', views.ParsingCreateView),
]

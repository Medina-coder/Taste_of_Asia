from django.urls import path
from category import views

urlpatterns = [
    path('', views.CommentListCreateView.as_view()),
    path('<int:pk>/delete/', views.FoodDeleteView.as_view()),

]
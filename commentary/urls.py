from django.urls import path

from commentary import views

urlpatterns = [
    path('', views.CommentaryListCreateView.as_view()),
    path('<int:pk>/', views.CommentaryDetailView.as_view()),
    path('<int:pk>/delete/', views.CommentaryDeleteView.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetailView.as_view()),
    path('', views.PostListCreateView.as_view())
]
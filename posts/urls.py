from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:pk>/', views.CommentDetailView.as_view()),
    path('<int:pk>/comment/', views.CommentListCreateView.as_view()),
    path('<int:pk>/upvote/', views.upvote_post),
    path('<int:pk>/', views.PostDetailView.as_view()),
    path('reset/', views.clear_upvotes),
    path('', views.PostListCreateView.as_view(), name='post_list')
]

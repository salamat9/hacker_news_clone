from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import reset_upvotes
from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment
from .serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer, \
                         CommentSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        else:
            return PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer.save(author=self.request.user, post=post)

    def list(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        queryset = Comment.objects.filter(post=post)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


@api_view(['POST', 'GET'])
def upvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    print(user.username)
    if user not in post.upvotes.all():
        post.upvotes.add(user)
        return Response(data={'message': 'Up voted!'}, status=status.HTTP_202_ACCEPTED)
    else:
        post.upvotes.remove(user)
        return Response(data={'message': 'Un voted!'}, status=status.HTTP_202_ACCEPTED)


@api_view(['POST', 'GET'])
def clear_upvotes(request):
    reset_upvotes()
    return Response(data={'message': 'Upvotes was cleared!'}, status=status.HTTP_202_ACCEPTED)








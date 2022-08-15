from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from posts.serializers import PostSerializer, PostUpdateSerializer
from posts.models import Post
import posts.json_placeholder_communication_service as jp


# Create your views here.

def create_new_id_for_post():
    count_of_posts = Post.objects.filter(id__gte=100).count()
    return 100 + count_of_posts + 1


def create_post(user_id, serializer):
    if jp.exists_user_with_id(user_id):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "user_id " + str(user_id) + " does not exists."}, status=status.HTTP_400_BAD_REQUEST)


def find_and_save_post(pk):
    post = jp.get_post_by_id(pk)

    if post is None:
        return Response({"detail:": "Post does not exists"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(data=post)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data["id"] = create_new_id_for_post()
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            return create_post(request.data["user_id"], serializer)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        try:
            post = self.get_object(pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Http404:
            return find_and_save_post(pk)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostUpdateSerializer(post, request.data)

        if serializer.is_valid():
            serializer.save()
            post = self.get_object(pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPostList(APIView):
    def get(self, request, user_id, format=None):
        posts = Post.objects.filter(user_id=user_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

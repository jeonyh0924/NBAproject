from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Post, Comment, HashTags
from ..serializers import PostSerializer


# def posts_list_api(request):
#     if request.method == 'GET':
#         post = Post.objects.all()
#         serializer = PostSerializer(post, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#
# @csrf_exempt
# def posts_detail_api(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoseNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data)
#
#     if request.method == 'PUT':
#         data = JSONParser.parse(request)
#         serializer = PostSerializer(post, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#     return JsonResponse(serializer.erros, status=400)
#

class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_objects(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_objects(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None, **kwargs):
        partial = kwargs.pop('partial', False)

        post = self.get_objects(pk)
        serializer = PostSerializer(post, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        return self.put(request, pk, format, partial=True)

    def delete(self, request, pk, format=None):
        post = self.get_objects(pk)
        post.delete()
        return Response(status.HTTP_204_NO_CONTENT)

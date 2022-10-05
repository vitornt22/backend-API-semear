

from project.models import Project
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Comment, Like, Publication
from .pagination import TimelineResultsPagination
from .serializers import (CommentSerializer, LikeSerializer,
                          PublicationSerializer)

# Create your views here.


class PublicationApi (ModelViewSet):
    queryset = Publication.objects.all().order_by('-created_at')
    serializer_class = PublicationSerializer
    pagination_class = TimelineResultsPagination
    ordering = ('created_at')

    @action(detail=True, methods=['GET'])
    def getCommentsNumber(self, request, pk,   * args, **kwargs):
        try:
            number = Comment.objects.filter(publication=pk).count()

            return Response({"number": number}, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({'number': 0}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def getLikesNumber(self, request, pk,   * args, **kwargs):
        try:
            # publication = Publication.objects.filter(pk=pk).first()
            number = Like.objects.filter(publication=pk).count()

            return Response({"number": number}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'number': 1020}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        post_data = request.data
        print("REQUEST PUBLICATION", request.data)

        try:
            user = UserModel.objects.get(id=post_data['id_user'])
            a = Project.objects.get(user=user)

            new_Publication = Publication.objects.create(
                project=a,
                id_user=post_data['id_user'],
                upload=request.FILES['upload'],
                legend=post_data['legend'],
                is_accountability=False,
            )

            new_Publication.save()
            serializer = PublicationSerializer(new_Publication)
            return Response(serializer.data, status=status.HTTP_200_OK
                            )
        except Project.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)  # noqa


class CommentApi (ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    ordering = ('created_at')

    @action(methods=['GET'], detail=True, )
    def getComments(self, request, pk, *args, **kwargs):
        if Publication.objects.filter(pk=pk).exists():
            comment = Comment.objects.filter(publication=pk)
            return Response(CommentSerializer(comment).data, status=status.HTTP_200_OK)  # noqa
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        post_data = request.data
        print("REQUEST PUBLICATION", request.data)

        try:
            user = UserModel.objects.get(id=post_data['user'])
            publication = Publication.objects.get(
                id=post_data['publication'])

            new_comment = Comment.objects.create(
                user=user,
                publication=publication,
                comment=post_data['comment']
            )

            new_comment.save()
            serializer = CommentSerializer(new_comment)
            return Response(serializer.data, status=status.HTTP_200_OK
                            )
        except Comment.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)  # noqa


class LikeApi (ModelViewSet):
    queryset = Like.objects.all().order_by('-created_at')
    serializer_class = LikeSerializer
    ordering = ('created_at')

    @action(methods=['GET'], detail=True)
    def deleteLike(self, request, pk, *args, **kwargs):
        pub = int(kwargs['publication'])
        if Like.objects.filter(user=pk, publication=pub).exists():
            like = Like.objects.get(user=pk, publication=pub)
            like.delete()
            pub = Publication.objects.get(id=pub)

            return Response(PublicationSerializer(pub).data, status=status.HTTP_200_OK)  # noqa
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        post_data = request.data
        print("REQUEST PUBLICATION", request.data)

        try:
            user = UserModel.objects.get(id=post_data['user'])
            publication = Publication.objects.get(
                id=post_data['publication'])

            new_comment = Like.objects.create(
                user=user,
                publication=publication,
                is_anonymous=post_data['is_anonymous'],
            )

            new_comment.save()

            publication = Publication.objects.get(
                id=post_data['publication'])

            serializer = PublicationSerializer(publication)

            return Response(serializer.data, status=status.HTTP_200_OK
                            )
        except Like.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)  # n

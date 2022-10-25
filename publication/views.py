

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

import publication
from publication.publicationSavedSerializer import PublicationSavedSerializer

from .models import Comment, Like, Publication, PublicationSaved
from .pagination import TimelineResultsPagination
from .serializers import (CommentSerializer, LikeSerializer,
                          PublicationSerializer)


# Create your views here.
class PublicationSavedApi(ModelViewSet):
    queryset = PublicationSaved.objects.all()
    serializer_class = PublicationSavedSerializer


class PublicationApi (ModelViewSet):
    queryset = Publication.objects.all().order_by('-created_at')
    serializer_class = PublicationSerializer
    pagination_class = TimelineResultsPagination
    ordering = ('created_at')

    @action(methods=['GET'], detail=True)
    def getMyPublications(self, request, pk, *args, **kwargs):
        user = UserModel.objects.get(id=pk)
        publications = Publication.objects.filter(user=user)
        print("PUBLICATIONS, ", publications)
        return Response(PublicationSerializer(publications, many=True).data, status=status.HTTP_200_OK)  # noqa

    @action(methods=['GET'], detail=True)
    def getLabelPublicationSaved(self, request, pk, *args, **kwargs):
        pub = int(kwargs['publication'])
        user = UserModel.objects.get(pk=pk)
        pub = Publication.objects.get(pk=pub)
        if PublicationSaved.objects.filter(user=user, publication=pub).exists():  # noqa
            return Response({"label": True})
        else:
            return Response({"label": False})

    @action(methods=['GET'], detail=True)
    def savePublication(self, request, pk, *args, **kwargs):
        try:
            pk2 = int(kwargs['publication'])
            user = UserModel.objects.get(pk=pk)
            pub = Publication.objects.get(pk=pk2)
            publicationSaved = PublicationSaved(user=user, publication=pub)
            publicationSaved.save()
            return Response({"check": True}, status=status.HTTP_200_OK)
        except:  # noqa
            return Response({"check": False}, status=status.HTTP_400_BAD_REQUEST)  # noqa

    @action(methods=['GET'], detail=True)
    def unSavePublication(self, request, pk, *args, **kwargs):
        try:
            pk2 = int(kwargs['publication'])
            user = UserModel.objects.get(pk=pk)
            pub = Publication.objects.get(pk=pk2)
            publicationSaved = PublicationSaved.objects.get(
                user=user, publication=pub)
            publicationSaved.delete()
            return Response({"check": True}, status=status.HTTP_200_OK)
        except:  # noqa
            return Response({"check": False}, status=status.HTTP_400_BAD_REQUEST)  # noqa

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

            new_Publication = Publication.objects.create(
                user=user,
                id_user=post_data['id_user'],
                upload=request.FILES['upload'],
                legend=post_data['legend'],
                is_accountability=bool(post_data['is_accountability']),
            )

            new_Publication.save()
            serializer = PublicationSerializer(new_Publication)
            return Response(serializer.data, status=status.HTTP_200_OK
                            )
        except UserModel.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)  # noqa


class CommentApi (ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    ordering = ('created_at')

    @action(methods=['GET'], detail=True)
    def deleteComment(self, request, pk, *args, **kwargs):
        pub = int(kwargs['publication'])
        if Comment.objects.filter(pk=pk).exists():
            like = Comment.objects.get(pk=pk)
            like.delete()
            pub = Publication.objects.get(id=pub)

            return Response(PublicationSerializer(pub).data, status=status.HTTP_200_OK)  # noqa
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

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
            publication = Publication.objects.get(
                id=post_data['publication'])
            serializer = PublicationSerializer(publication)

            return Response(serializer.data, status=status.HTTP_200_OK
                            )
        except Comment.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)  # noqa


class LikeApi (ModelViewSet):
    queryset = Like.objects.all().order_by('-created_at')
    serializer_class = LikeSerializer
    ordering = ('created_at')

    @action(methods=['GET'], detail=True)
    def isLiked(self, request, pk, *args, **kwargs):
        pub = int(kwargs['publication'])
        if Like.objects.filter(user=pk, publication=pub).exists():
            return Response({"label": "Descurtir"})
        else:
            return Response({"label": "Curtir"})

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

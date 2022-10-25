

# flake8: noqa E722, E501
from os import stat

from church.models import Church
from informations.models import Adress
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel
from user.serializers import UserSerializer

from .followerserializer import FollowerSerializer
from .models import Follower, Project
from .serializers import ProjectSerializer


class FollowerApi(ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    @action(methods=['GET'], detail=True)
    def searchFollower(self, request, pk, *args, **kwargs):
        search = int(kwargs['search'])
        category = int(kwargs['category'])

        if (category == 'following'):
            listFollower = Follower.objects.filter(user=pk)

    @action(methods=['GET'], detail=True)
    def getLabelFollower(self, request, pk, *args, **kwargs):
        pk2 = int(kwargs['pk2'])
        user = UserModel.objects.get(pk=pk)
        user2 = UserModel.objects.get(pk=pk2)
        if Follower.objects.filter(user=user, user2=user2).exists():
            return Response({"label": True})
        else:
            return Response({"label": False})

    @action(methods=['GET'], detail=True)
    def setFollower(self, request, pk, *args, **kwargs):
        pk2 = int(kwargs['pk2'])
        user = UserModel.objects.get(pk=pk)
        user2 = UserModel.objects.get(pk=pk2)
        follower = Follower(user=user, user2=user2)
        follower.save()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def unFollower(self, request, pk, *args, **kwargs):

        pk2 = int(kwargs['pk2'])
        user = UserModel.objects.get(pk=pk)
        user2 = UserModel.objects.get(pk=pk2)
        follower = Follower.objects.get(user=user, user2=user2)
        follower.delete()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def getFollowers(self, request, pk, *args, **kwargs):
        try:
            followers = Follower.objects.filter(user2=pk)
            if len(followers) == 0:
                response = {}
            else:
                response = FollowerSerializer(
                    followers.order_by('-created_at'), many=True).data
            return Response(response, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def getFollowing(self, request, pk, *args, **kwargs):
        try:
            followers = Follower.objects.filter(user=pk)
            if len(followers) == 0:
                response = {}
            else:
                response = FollowerSerializer(
                    followers.order_by('-created_at'), many=True).data
            return Response(response, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class ProjectApi (ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['GET'], )
    def getprojectData(self, request, pk):
        try:
            user = UserModel.objects.filter(id=pk).first()
            project = Project.objects.filter(user=user).first()
            if project is not None:
                return Response(ProjectSerializer(project).data, status=status.HTTP_200_OK)
            else:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = Project.objects.all()
        print('EAI')
        ProjectSerializer(
            queryset, context={'current_user': 1}, many=True)

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        post_data = request.data

        adressCheck = post_data["id_adress"]

        if post_data["adress"] is None:
            adress = Adress.objects.get(id=adressCheck)
        else:
            adress = Adress.objects.create(
                adress=post_data["adress"]["adress"],
                zip_code=post_data["adress"]["zip_code"],
                number=post_data["adress"]["number"],
                city=post_data["adress"]["city"],
                uf=post_data["adress"]['uf'],
                district=post_data["adress"]['district']
            )
            adress.save()

        new_user = UserModel.objects.create_superuser(
            post_data['user']['category'],
            post_data['user']['username'],
            True,
            post_data["user"]["email"],
            post_data["user"]["password"]
        )

        if post_data['id_church'] != 0:
            church = Church.objects.get(id=post_data['id_church'])
        else:
            church = Church.objects.get(id=post_data['id_church'])

        new_Project = Project.objects.create(
            user=new_user,
            adress=adress,
            church=church,
            id_church=post_data['id_church'],
            id_adress=post_data['id_adress'],
            name=post_data['name'],

        )

        new_Project.save()
        serializer = ProjectSerializer(new_Project)

        return Response(serializer.data)

    def get_serializer_context(self):
        context = super(ProjectApi, self).get_serializer_context()
        context.update({"current_user": 1})
        return context

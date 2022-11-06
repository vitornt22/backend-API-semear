# flake8: noqa: E501
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import publication
from donor.models import Donor
from missionary.models import Missionary
from missionary.serializers import MissionarySerializer
from project.models import Project
from project.serializers import ProjectSerializer
from publication.models import Like
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Information, UserModel
from .serializers import InformationSerializer, UserSerializer


class InformationApi (ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    def create(self, request, *args, **kwargs):
        a = super().create(request, *args, **kwargs)
        if 'id' in request.data:
            id = request.data['id']
            print(id)
            user = UserModel.objects.get(id=id)
            information = Information.objects.get(id=a.data['id'])
            print(a.data)
            if (user.category == 'project'):
                project = Project.objects.get(user=id)
                project.information = information
                project.save()
                return Response(ProjectSerializer(project).data, status=status.HTTP_200_OK)
            elif (user.category == 'missionary'):
                missionary = Missionary.objects.get(user=id)
                missionary.information = information
                missionary.save()
                return Response(MissionarySerializer(missionary).data, status=status.HTTP_200_OK)

        return Response({'this': 'teste'})


class UserApi (ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @action(methods=['GET'], detail=True)
    def getButtonLike(self, request, pk, *args, **kwargs):
        pub = int(kwargs['target_id'])
        print(pub)
        if Like.objects.filter(user=pk, publication=pub).exists():
            return Response({"label": "Descurtir"})
        else:
            return Response({"label": "Descurtir"})

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @action(methods=['GET'], detail=False)
    def changePassword(self, request, email, pk, *args, **kwargs):
        host = "smtp.gmail.com"
        port = '587'
        login = 'aplicativosemear@gmail.com'
        senha = "gkpqxtlkrpnmhvgb"

        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(login, senha)

        # MONTANDO EMAIL
        corpo = 'olá'
        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = email
        email_msg['Subject'] = "Codigo para mudança de senha "
        email_msg.attach(MIMEText(corpo, 'text'))

        # ENVIANDO EMAIL

        try:
            server.sendmail(email_msg['From'],
                            email_msg['To'], email_msg.as_string())
            server.quit()

        except:
            ...


class checkEmail(generics.RetrieveAPIView):
    lookup_field = 'email'
    lookup_url_kwarg = 'email'
    queryset = UserModel.objects.all()
    serializer = UserSerializer

    def get(self, request, email, *args, **kwargs):
        print('EMAIL:', email)
        try:
            a = UserModel.objects.filter(email=email).exists()
        except UserModel.DoesNotExist:
            a = False

        return Response({'check': a})


class checkUsername(generics.RetrieveAPIView):
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    queryset = UserModel.objects.all()
    serializer = UserSerializer

    def get(self, request, username, *args, **kwargs):
        print('EMAIL:', username)
        try:
            a = UserModel.objects.filter(username=username).exists()
        except UserModel.DoesNotExist:
            a = False

        return Response({'check': a})


class getCategory(generics.RetrieveAPIView):
    lookup_field = 'email'
    lookup_url_kwarg = 'email'
    queryset = UserModel.objects.all()
    serializer = UserSerializer

    def get(self, request, email, *args, **kwargs):
        print('EMAIL:', email)

        try:
            a = UserModel.objects.get(email=email)
            serializer = UserSerializer(a).data
            print('SERIALIZER')
            return Response({'user': serializer}, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response({'user': None}, status=status.HTTP_404_NOT_FOUND)

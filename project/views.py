

from church.models import Church
from informations.models import Adress
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Project
from .serializers import ProjectSerializer


class ProjectApi (ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        queryset = Project.objects.all()
        print('EAI')
        a = ProjectSerializer(
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

        church = Church.objects.get(id=post_data['id_church'])

        new_Project = Project.objects.create(
            user=new_user,
            adress=adress,
            church=church,
            id_church=post_data['id_church'],
            id_adress=post_data['id_adress'],
            name=post_data['name'],
            followers=[],
            following=[]
        )

        new_Project.save()
        serializer = ProjectSerializer(
            new_Project, many=True)

        return Response(serializer.data)

    def get_serializer_context(self):
        context = super(ProjectApi, self).get_serializer_context()
        context.update({"current_user": 1})
        return context

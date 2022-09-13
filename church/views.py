# flake8: noqa: E501
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Church
from .serializers import ChurchSerializer


class ChurchApiViewSet(ModelViewSet):
    serializer_class = ChurchSerializer
    queryset = Church.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({
            "user": Church(user, context=self.get_serializer_context()).data,
        })

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Register API
class RegisterChurchAPI(generics.GenericAPIView):
    serializer_class = ChurchSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Create an Authentication Token for the user
        # Create an Authentication Token for the user
       # token = AuthToken.objects.create(user)[1]

        return Response({
            "user": ChurchSerializer(user, context=self.get_serializer_context()).data,
            # "token": token
        })

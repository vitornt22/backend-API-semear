# flake8: noqa: F401
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

user_api_router = SimpleRouter()
user_api_router.register(
    'church/api',
    views.ChurchViewSet,
    'church'
)

urlpatterns = user_api_router.urls
print(urlpatterns)

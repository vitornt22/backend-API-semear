from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = "project"

user_api_router = SimpleRouter()
user_api_router.register(
    'project/api', views.ProjectApi,
    basename='project'
)
follower_api_router = SimpleRouter()
follower_api_router.register(
    'follower/api', views.FollowerApi,
    basename='follower'
)

urlpatterns = [
    path('project/api/<int:pk>/setFollower/<int:pk2>/',
         views.FollowerApi.as_view({"get": "setFollower"})),
    path('project/api/<int:pk>/unFollower/<int:pk2>/',
         views.FollowerApi.as_view({"get": "unFollower"})),
    path('follower/api/<int:pk>/getLabelFollower/<int:pk2>/',
         views.FollowerApi.as_view({"get": "getLabelFollower"})),
    path('follower/api/<int:pk>/<str:search>/searchFollower/<str:category>/',
         views.FollowerApi.as_view({"get": "getLabelFollower"})),



]


urlpatterns += user_api_router.urls + follower_api_router.urls

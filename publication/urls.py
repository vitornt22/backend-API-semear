from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = "publication"

publication_api_router = SimpleRouter()
publication_api_router.register(
    'publication/api', views.PublicationApi,
    basename='Publication'
)

comment_api_router = SimpleRouter()
comment_api_router.register(
    'comment/api', views.CommentApi,
    basename='Comment'
)

like_api_router = SimpleRouter()
like_api_router.register(
    'like/api', views.LikeApi,
    basename='Like'
)
urlpatterns = [
    path('like/api/<int:pk>/deleteLike/<int:publication>/',
         views.LikeApi.as_view({"get": "deleteLike"})),
    path('comment/api/<int:pk>/deleteComment/<int:publication>/',
         views.CommentApi.as_view({"get": "deleteComment"})),
]
urlpatterns += publication_api_router.urls + \
    like_api_router.urls + comment_api_router.urls

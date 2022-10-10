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

publicationSaved_api_router = SimpleRouter()
publicationSaved_api_router.register(
    'publicationSaved/api', views.PublicationSavedApi,
    basename='PublicationSaved'
)

like_api_router = SimpleRouter()
like_api_router.register(
    'like/api', views.LikeApi,
    basename='Like'
)
urlpatterns = [
    path('like/api/<int:pk>/deleteLike/<int:publication>/',
         views.LikeApi.as_view({"get": "deleteLike"})),
    path('like/api/<int:pk>/isLiked/<int:publication>/',
         views.LikeApi.as_view({"get": "isLiked"})),
    path('comment/api/<int:pk>/deleteComment/<int:publication>/',
         views.CommentApi.as_view({"get": "deleteComment"})),
    path('publication/api/<int:pk>/savePublication/<int:publication>/',
         views.PublicationApi.as_view({"get": "savePublication"})),
    path('publication/api/<int:pk>/unSavePublication/<int:publication>/',
         views.PublicationApi.as_view({"get": "unSavePublication"})),
]
urlpatterns += publication_api_router.urls + \
    like_api_router.urls + comment_api_router.urls

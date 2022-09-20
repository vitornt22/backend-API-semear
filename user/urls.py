from django.urls import path
from rest_framework.routers import SimpleRouter

from user import views

app_name = "user"


user_api_router = SimpleRouter()
user_api_router.register(
    'user/api', views.UserApi,
    basename='user'
)
urlpatterns = [
    path('user/api/<str:email>/checkEmail/',
         views.checkEmail.as_view(), name='checkEmail'),

    path('user/api/<str:username>/checkUsername/',
         views.checkUsername.as_view(), name='checkUsername')
]

urlpatterns += user_api_router.urls

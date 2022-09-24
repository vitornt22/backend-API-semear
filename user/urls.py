from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

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
         views.checkUsername.as_view(), name='checkUsername'),
    path('user/api/<str:email>/getUserData/',
         views.getCategory.as_view(), name='getCategory'),

    path('user/api/token/',
         TokenObtainPairView.as_view(), name='token_obtain_par'),
    path('user/api/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh_par'),
    path('user/api/token/verify/',
         TokenVerifyView.as_view(), name='token_verify_par'),
]

urlpatterns += user_api_router.urls

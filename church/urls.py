# flake8: noqa: F401
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from . import views

name = 'church'
urlpatterns = [
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
user_api_router = SimpleRouter()
user_api_router.register(
    'api',
    views.ChurchApiViewSet,
    'church'
)

urlpatterns += user_api_router.urls
print(urlpatterns)

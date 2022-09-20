from django.urls import path
from rest_framework.routers import SimpleRouter

from church import views

app_name = "church"

user_api_router = SimpleRouter()
user_api_router.register(
    'church/api', views.ChurchApi,
    basename='church'
)
print(user_api_router.urls)

urlpatterns = [
    path('church/api/<str:cnpj>/getChurchAddress/',
         views.getChurchAddress.as_view(), name='getChurchAddress'), ]

urlpatterns += user_api_router.urls

from rest_framework.routers import SimpleRouter

from . import views

app_name = "donor"

user_api_router = SimpleRouter()
user_api_router.register(
    'donor/api', views.DonorApi,
    basename='donor'
)
urlpatterns = user_api_router.urls

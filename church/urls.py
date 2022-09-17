from rest_framework.routers import SimpleRouter

from . import views

app_name = "church"

user_api_router = SimpleRouter()
user_api_router.register(
    'church/api', views.ChurchApi,
    basename='church'
)
urlpatterns = user_api_router.urls

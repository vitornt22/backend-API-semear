from rest_framework.routers import SimpleRouter

from . import views

app_name = "publication"

user_api_router = SimpleRouter()
user_api_router.register(
    'publication/api', views.PublicationApi,
    basename='Publication'
)
urlpatterns = user_api_router.urls

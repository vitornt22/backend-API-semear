from rest_framework.routers import SimpleRouter

from user import views

app_name = "user"

user_api_router = SimpleRouter()
user_api_router.register(
    'user/api', views.UserApi,
    basename='user'
)
urlpatterns = user_api_router.urls

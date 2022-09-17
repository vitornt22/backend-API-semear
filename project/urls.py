from rest_framework.routers import SimpleRouter

from . import views

app_name = "project"

user_api_router = SimpleRouter()
user_api_router.register(
    'project/api', views.ProjectApi,
    basename='project'
)
urlpatterns = user_api_router.urls

from rest_framework.routers import SimpleRouter

from . import views

app_name = "missionary"

missionary_api_router = SimpleRouter()
missionary_api_router.register(
    'missionary/api', views.MissionaryApi,
    basename='missionary'
)
urlpatterns = missionary_api_router.urls

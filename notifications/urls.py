from rest_framework.routers import SimpleRouter

from . import views

app_name = "notification"

notification_api_router = SimpleRouter()
notification_api_router.register(
    'notification/api', views.notificationApi,
    basename='notification'
)
urlpatterns = notification_api_router.urls

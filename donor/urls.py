from rest_framework.routers import SimpleRouter

from . import views

app_name = "donor"

donor_api_router = SimpleRouter()
donor_api_router.register(
    'donor/api', views.DonorApi,
    basename='donor'
)
urlpatterns = donor_api_router.urls

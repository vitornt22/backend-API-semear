from rest_framework.routers import SimpleRouter

from . import views

app_name = "informations"

adress_api_router = SimpleRouter()
adress_api_router.register(
    'adress/api', views.AdressApi,
    basename='adress'
)

bankData_api_router = SimpleRouter()
bankData_api_router.register(
    'bankData/api', views.BankDataApi,
    basename='bankData'
)
urlpatterns = bankData_api_router.urls + adress_api_router

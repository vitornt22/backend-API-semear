from rest_framework.routers import SimpleRouter

from . import views

app_name = "transaction"

transaction_api_router = SimpleRouter()
transaction_api_router.register(
    'transaction/api', views.TransactionApi,
    basename='transaction'
)
urlpatterns = transaction_api_router.urls

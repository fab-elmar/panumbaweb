from django.urls import path, include

from .views import AIcontactListView


app_name = "interface"
urlpatterns = [
    path("", AIcontactListView.as_view(), name="index"),
    # path("api/", include("panumbaweb.interface.api.urls", namespace="api")),
]

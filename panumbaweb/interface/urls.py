from django.urls import path, include

from .views import AIcontactListView, PanumbaQuestionView, ShowNumberView
from interface.api.views import LatestAnswerAPI

app_name = "interface"
urlpatterns = [
    path("list/", AIcontactListView.as_view(), name="list"),
     path("", PanumbaQuestionView.as_view(), name="index"),
    path("question/", PanumbaQuestionView.as_view(), name="question"),
    path('show-number/', ShowNumberView.as_view(), name='show_number'),
    path('api/latest-answer/', LatestAnswerAPI.as_view(), name='api_latest_answer'),
   # path('world-population/', WorldPopulationView.as_view(), name='world_population'),
    #path("api/", include("panumbaweb.interface.api.urls", namespace="api")),
]

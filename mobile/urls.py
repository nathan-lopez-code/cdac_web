from django.urls import path
from . views import InformationList


app_name = "api"


urlpatterns = [
    path("all/information", InformationList.as_view(), name="getInformation"),
]

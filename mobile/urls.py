from django.urls import path
from . views import get_information


app_name = "mobile_app"


urlpatterns = [
    path("/get/all/information", get_information, name="getInformation"),
]

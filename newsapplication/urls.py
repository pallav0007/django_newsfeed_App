from django.urls import path
from . import views

urlpatterns = [
    path("/<country>/<category>",views.universal,name="universal"),

    path("",views.home,name='home'),
    path("sports/",views.homesp,name="sports"),
    path("usports/",views.homeusp,name="usports"),
    path("us/",views.homeus,name="us"),
]
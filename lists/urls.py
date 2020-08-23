from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("toggle/<int:room_pk>", views.toogle_room, name="toogle-room"),
    path("favs/", views.SeeFavsView.as_view(), name="see-favs"),
]


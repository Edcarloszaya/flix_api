from django.urls import path

from . import views

urlpatterns = [
    path(
        "actors/", views.ActorCreateListView.as_view(), name="actors-list-create-view"
    ),
    path(
        "actors/<int:pk>",
        views.ActorRetrieveUpdateDestroyView.as_view(),
        name="actors-retrive-update-destroy-view",
    ),
]

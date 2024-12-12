from django.urls import path

from . import views

urlpatterns = [
    path(
        "genres/", views.GenreCreateListView.as_view(), name="genre-create-liste-view"
    ),
    path(
        "genres/<int:pk>",
        views.GenreRetrieveUpdateDestroyView.as_view(),
        name="genre_detail-view",
    ),
]

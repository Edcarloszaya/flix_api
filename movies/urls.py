from django.urls import path

from . import views

urlpatterns = [
    path(
        "movies/", views.MovieCreateListeView.as_view(), name="movie-list-create-view"
    ),
    path(
        "movies/<int:pk>",
        views.MovieRetrieveUpdateDestroyView.as_view(),
        name="movie-retrive-update-destroy-view",
    ),
    path("movies/stats/", views.MovieStatsView.as_view(), name="movie-stats-view"),
]

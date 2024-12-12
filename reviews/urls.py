from django.urls import path

from . import views

urlpatterns = [
    path(
        "reviews/",
        views.ReviewCreateListView.as_view(),
        name="reviews-list-create-view",
    ),
    path(
        "reviews/<int:pk>",
        views.ReviewRetrieveUpdateDestroyView.as_view(),
        name="reviews-retrive-update-destroy-view",
    ),
]

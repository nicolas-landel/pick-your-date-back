from django.urls import path

from place import views

urlpatterns = [
    path("", views.PlaceListView.as_view(), name="places"),
    path("place_answers/", views.AnswerPlaceView.as_view(), name="place_answers"),
    path("place_comments/", views.CommentPlaceView.as_view(), name="place_comments"),
    path("place_options/", views.OptionPlaceView.as_view(), name="place_options"),
]

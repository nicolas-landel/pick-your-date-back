from django.urls import path
from place import views

# define the urls
urlpatterns = [
    path("", views.PlaceListView.as_view(), name="places"),
]

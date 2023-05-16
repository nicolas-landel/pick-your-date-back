from django.conf.urls import include
from django.urls import path, re_path

from user.views import GetUserView, ListUserMembers, UserCreateView, UserLoginView

urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^login/$", UserLoginView.as_view(), name="user-login"),
    re_path(r"^signup/$", UserCreateView.as_view(), name="user-creation"),
    path("<uuid:pk>/", GetUserView.as_view(), name="user"),
    path("members/", ListUserMembers.as_view(), name="place-members"),
]

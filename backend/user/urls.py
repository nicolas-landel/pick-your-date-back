from django.conf.urls import include
from django.urls import re_path
from user.views import UserCreateView, UserLoginView

urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^login/$", UserLoginView.as_view(), name="user-login"),
    re_path(r"^signup/$", UserCreateView.as_view(), name="user-creation"),
]

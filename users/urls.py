from django.urls import path
from .views import UserHomeView,UserRegisterView,UserLoginView,UserLogoutView,UserDataCreateView

app_name = "users"

urlpatterns = [
    path("", UserHomeView.as_view(), name="home"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("data/", UserDataCreateView.as_view(), name="data"),
]
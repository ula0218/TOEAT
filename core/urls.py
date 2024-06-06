from django.contrib import admin
from django.urls import path,include
from .views import UserTemplateView

urlpatterns = [
    path("", UserTemplateView.as_view(), name="home"),
    path("users/", include("users.urls")),
    path("todos/", include("todos.urls")),
    path("events/", include("events.urls")),
    path("menus/", include("menus.urls")),
    path("admin/", admin.site.urls),
]

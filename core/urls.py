from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("users/", include("users.urls")),
    path("todos/", include("todos.urls")),
    path("admin/", admin.site.urls),
]

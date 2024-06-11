from django.urls import path
from .views import TodoCreateView,TodoListView,TodoStatsView

app_name = "todos"

urlpatterns = [
    path("create/",TodoCreateView.as_view(),name ="create"),
    path("list/",TodoListView.as_view(),name ="list"),
    path('chart/', TodoStatsView.as_view(), name='chart'),
]
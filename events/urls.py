from django.urls import path
from .views import CalendarView

app_name='events'

urlpatterns = [
    path('view/', CalendarView.as_view(), name='view'),
]
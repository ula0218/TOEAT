from django.urls import path
from .views import CategorySelectionView

app_name='menus'

urlpatterns = [
    path('create/', CategorySelectionView.as_view(), name='create'),
]
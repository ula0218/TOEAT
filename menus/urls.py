from django.urls import path
from .views import CategorySelectionView,MapView

app_name='menus'

urlpatterns = [
    path('create/', CategorySelectionView.as_view(), name='create'),
    path('map/', MapView.as_view(), name='map'),
]
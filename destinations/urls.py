from django.urls import path, include
from . import views
from .views import DestinationListView

urlpatterns = [
	path('', views.home, name='home'),
	path('destinations/', DestinationListView.as_view(), name='destinations'),
]
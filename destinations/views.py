from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Destination

# Create your views here.
def home(request):
	return render(request, 'destinations/home.html')

class DestinationListView(ListView):
	model = Destination
	paginate_by = 10

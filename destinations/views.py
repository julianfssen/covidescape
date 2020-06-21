from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Destination

# Create your views here.
def home(request):
	return render(request, 'destinations/home.html')

class DestinationListView(ListView):
	model = Destination
	fields = ['region']
	template_name = 'destinations/destination_list.html'
	paginate_by = 10

	def get_queryset(self):
		region = self.request.GET.get('region', 'asia')
		context = Destination.objects.filter(region__iexact = region)
		return context

	def get_context_data(self, **kwargs):
		context = super(DestinationListView, self).get_context_data(**kwargs)
		context['region'] = self.request.GET.get('region', 'asia')
		return context
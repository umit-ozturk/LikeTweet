from django.shortcuts import render
from django.views.generic  import DetailView, ListView
from .models import Tweet
# Create your views here.


#Create

#Update

#Delete

#Retrieve



# Defaul Template Path "tweets/detail_view.html"
class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

	#pk = self.kwargs.get("pk")

	#def get_object(self):
	#	return Tweet.objects.get(id=pk )


class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		### print(context) --> We see tweet data.
		return context
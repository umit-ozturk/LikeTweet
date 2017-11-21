from django.shortcuts import render, get_object_or_404
from django.views.generic  import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .models import Tweet
# Create your views here.


#Create
class TweetCreateView(CreateView):
	form_class  = TweetModelForm
	template_name = "tweets/create_view.html"
	success_url = "/tweet/create"
	def form_valid(self, form):
		form.instance .user = self.request.user
		return super(TweetCreateView, self).form_valid(form)
		
## Aynı şey fakat birde functional tabanlı yapalım

#def tweet_create_view(request):
#	form = TweetModelForm(request.POST or None) 
#	if form.is_valid():
#		instance = form.save(commit = False)
#		instance.user = request.user
#		instance.save()
#	context = {
#		"form" : form
#	}
#	return render(request, "tweets/create_view.html", context)



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
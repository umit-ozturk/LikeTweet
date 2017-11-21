from django.contrib.auth.mixins import LoginRequiredMixin # Dont using now
from django.shortcuts import render, get_object_or_404
from django.views.generic  import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from .models import Tweet
# Create your views here.


#Create
class TweetCreateView(FormUserNeededMixin, CreateView): #LoginRequiredMixin importing class auto authenticated validation
	form_class  = TweetModelForm
	template_name = "tweets/create_view.html"
	success_url = "/tweet/create" 
	#login_url = "/admin/". # About LoginRequiredMixin redirect to admin 



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
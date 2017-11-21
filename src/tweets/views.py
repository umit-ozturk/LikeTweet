from django.contrib.auth.mixins import LoginRequiredMixin # Dont using now
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic  import (
			CreateView,
			DetailView, 
			DeleteView,
			ListView,
			UpdateView
			)
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet

#Create
class TweetCreateView(FormUserNeededMixin, CreateView): #LoginRequiredMixin importing class auto authenticated validation
	form_class  = TweetModelForm
	template_name = "tweets/create_view.html"
	success_url = "/tweet/create/" 
	#login_url = "/admin/". # About LoginRequiredMixin redirect to admin 
#Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class  = TweetModelForm
	template_name = "tweets/update_view.html"
	success_url = "/tweet/"
#Delete
class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	template_name = "tweets/delete_confirm.html"
	success_url = reverse_lazy("home")
#Retrieve
class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()
#List
class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		return context
		
def tweet_detail_view(request, pk=None):
	obj = get_object_or_404(Tweet, pk=pk)
	context = {
		"object" : obj
	}
from django.contrib.auth.mixins import LoginRequiredMixin # Dont using now
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
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


#Retweet

class RetweetView(View):
	def get(self, request, pk, *args, **kwargs):
		tweet = get_object_or_404(Tweet, pk=pk)
		print(pk + str(tweet))
		if request.user.is_authenticated():
			new_tweet = Tweet.objects.retweet(request.user, tweet)
			return HttpResponseRedirect("/")
		return HttpResponseRedirect(tweet.get_absolute_url())
#Create
class TweetCreateView(FormUserNeededMixin, CreateView): #LoginRequiredMixin importing class auto authenticated validation
	form_class  = TweetModelForm
	template_name = "tweets/create_view.html"
#	success_url = reverse_lazy("tweet:detail")
	#login_url = "/admin/". # About LoginRequiredMixin redirect to admin 
#Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class  = TweetModelForm
	template_name = "tweets/update_view.html"
	#success_url = "/tweet/"
#Delete
class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	template_name = "tweets/delete_confirm.html"
	success_url = reverse_lazy("tweet:list")
#Retrieve
class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()
#List
class TweetListView(ListView):
	queryset = Tweet.objects.all()
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.order_by('-timestamp')
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
				)
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = TweetModelForm
		context['create_url'] = reverse_lazy("tweet:create")
		return context
		

##.  Functional View Not İmportant 

def tweet_detail_view(request, pk=None):
	obj = get_object_or_404(Tweet, pk=pk)
	context = {
		"object" : obj
	}
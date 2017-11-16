from django.shortcuts import render

from .models import Tweet
# Create your views here.


#Create

#Update

#Delete

#Retrieve




### Functional based views. Actually functional based views not usefull. Therefore we will write Class Based Views at the next time.
def tweet_detail_view(request, id=1):
	obj = Tweet.objects.get(id=id) #Get from DATABASE
	print(obj)
	context = {
		"object" : obj
	}
	return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request):
	queryset = Tweet.objects.all()
	print(queryset)
	for obj in queryset:
		print(obj.content)
	context = {
		"object_list" : queryset
	}
	return render(request, "tweets/list_view.html", context)
from django.conf.urls import url


from .views import  (
	UserDetailView,
	UserFollowView
	)

urlpatterns = [
	url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name="detail"), #/tweet/1
	url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name="follow"), #/tweet/1

]



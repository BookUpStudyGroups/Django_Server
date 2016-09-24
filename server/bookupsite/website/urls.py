from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^class/$', views.listOfClasses),
	url(r'^group/$', views.GroupList.as_view()),
	url(r'^userz/$', views.UserList.as_view()),
	url(r'^buddies/$', views.StuddyBuddyList.as_view()),
	url(r'^messages/$', views.MessageList.as_view()),
	url(r'^userz/(?P<user_id>[0-9]+)/$', views.indUser.as_view()),
	url(r'^buddies/(?P<buddie_id>[0-9]+)/$', views.indBuddie.as_view()),
	url(r'^group/(?P<group_id>[0-9]+)/$', views.indGroup.as_view()),
	url(r'^class/(?P<pk>[0-9]+)/$', views.indClass),
	url(r'^messages/(?P<message_id>[0-9]+)/$', views.indMessage.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^class$', views.ClassList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
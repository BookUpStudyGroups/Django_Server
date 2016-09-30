from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework.decorators import api_view


# Create your views here.

def index(request):
	all_users = UserBuddy.objects.all()
	html = ''
	for userz in all_users:
		url = '/bookupsite/userz/' + str(userz.id) + '/'
		html += '<a href="' +url+ '">'+userz.user.username+'</a><br>'


	#return HttpResponse("<h1>This is the bookup app homepage</h1>")
	return HttpResponse(html)

class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
    	content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)


# TODO: add post classes
#TODO: add authentication

#lists all classes or creates a new one

# returns individual objects from data base as JSON
class indUser(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	def get(self, request, user_id,  format=None):
		test = UserBuddy.objects.filter(user__username=request.user)	
		serializer = AllUserBuddySerializer(test, many=True)
		return Response(serializer.data)

class indClass(APIView):
	def get(self, request, pk):
		thisClass = Class.objects.get(pk=pk)
		serializer = ClassSerializer(thisClass)
		return Response(serializer.data)


	#def perform_create()
	
	def post(self):
		pass


class indBuddie(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request, buddie_id):
		test = StudyBuddy.objects.filter(user1__user__username=request.user)
		serializer = AllStudyBuddySerializer(test, many=True)
		return Response(serializer.data)


	def post():
		pass

class indGroup(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request, group_id):
		thisgroup = Groups.objects.get(pk=group_id)
		serializer = GroupSerializer(thisgroup)
		return Response(serializer.data)
	def post():
		pass

class indMessage(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request, message_id):
		thisMessage = Message.objects.get(pk=message_id)
		serializer = GroupSerializer(thisMessage)
		return Response(serializer.data)




#Returns lists of objects from database as JSON

class ClassList(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		classes = Class.objects.all()
		serializer = ClassSerializer(classes, many=True)
		return Response(serializer.data)

	def post(self):
		pass


class GroupList(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		groups = Groups.objects.all()
		serializer = GroupSerializer(groups, many=True)
		return Response(serializer.data)

	def post(self):
		pass
class UserList(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		userlist = UserBuddy.objects.all()
		serializer = UserBuddySerializer(userlist, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class StuddyBuddyList(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request, buddie_id):
		test = StudyBuddy.objects.filter(user1__user__username=request.user)
		serializer = AllStudyBuddySerializer(test, many=True)
		return Response(serializer.data)


	def post():
		pass

class MessageList(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		messagelist = Message.objects.filter(author__user__username=request.user)
		serializer = MessageSerializer(messagelist, many=True)
		return Response(serializer.data)
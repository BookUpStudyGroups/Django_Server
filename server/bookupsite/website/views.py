from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework.decorators import api_view


# Create your views here.

################################################################
#Abstract: This file is handle requests based on a specific URL#
#the majority of these classes are to return information for   #
#the REST API, as the view returns JSON                        #
#Here is also where functions for html and templates exist     #
################################################################

#basic html return for testing
def index(request):
	all_users = UserBuddy.objects.all()
	html = ''
	for userz in all_users:
		url = '/bookupsite/userz/' + str(userz.id) + '/'
		html += '<a href="' +url+ '">'+userz.user.username+'</a><br>'

	return HttpResponse(html)

#basic user authentication for testing
class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
    	content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)

#Returns information concerning the certain user
class indUser(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	def get(self, request,  format=None):
		test = UserBuddy.objects.filter(user__username=request.user)	
		serializer = AllUserBuddySerializer(test, many=True)
		return Response(serializer.data)
	def post(self, request, *args, **kwargs):
		serializer = AllUserBuddySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#Returns information for a specific budy
class indBuddie(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request, buddie_id):
		test = StudyBuddy.objects.filter(user1__user__username=request.user)
		serializer = AllStudyBuddySerializer(test, many=True)
		return Response(serializer.data)


	def post(self,request, buddie_id, format=None):
		serializer = AllStudyBuddySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#Returns information for a specific group
class indGroup(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request, group_id):
		thisgroup = Groups.objects.get(pk=group_id)
		serializer = GroupSerializer(thisgroup)
		return Response(serializer.data)
	def post():
		pass
#This is a problem child
class indMessage(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request, message_id):
		thisMessage = Message.objects.get(pk=message_id)
		serializer = GroupSerializer(thisMessage)
		return Response(serializer.data)
	def post():
		pass
#returns all of the classes in the database
class ClassList(APIView):
	#authentication_classes = (SessionAuthentication, BasicAuthentication)
	#permission_classes = (IsAuthenticated,)
	def get(self, request):
		classes = Class.objects.all()
		serializer = ClassSerializer(classes, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		serializer = BetterClassSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


#Returns all of the groups so the user may pick from them to join
class GroupList(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		groups = Groups.objects.all()
		serializer = GroupSerializer(groups, many=True)
		return Response(serializer.data)

	def post(self):
		pass
#returns the list of study buddies that the user has
class StuddyBuddyList(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request, buddie_id):
		test = StudyBuddy.objects.filter(user1__user__username=request.user)
		serializer = AllStudyBuddySerializer(test, many=True)
		return Response(serializer.data)


	def post():
		pass
#returns all of the messages related to the user
class MessageList(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		messagelist = Message.objects.filter(author__user__username=request.user)
		serializer = MessageSerializer(messagelist, many=True)
		return Response(serializer.data)




#Still need to implement this
#essentiall return the messages of a group if the user is part of that group
class MessageListByGroup(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	def get(self,name, request):
		messagelist = Message.objects.filter(group__name=name)
		serializer = MessageSerializer(messagelist, many=True)
		return Response(serializer.data)

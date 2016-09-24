from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
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


@api_view(['GET', 'POST'])
def listOfClasses(request):

	if (request.method == 'GET'):
		classList = Class.objects.all()
		serializer = ClassSerializer(classList, many=True)
		return Response(serializer.data)

	elif(request.method == 'POST'):
		serializer = ClassSerializer(data=request.data)
		if (serializer.isvalid()):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO: add post classes
#TODO: add authentication

#lists all classes or creates a new one

# returns individual objects from data base as JSON
class indUser(APIView):
	def get(self, request, user_id):
		thisUser = UserBuddy.objects.get(pk=user_id)
		serializer = AllUserBuddySerializer(thisUser)
		return Response(serializer.data)

class indClass(APIView):
	def get(self, request, class_id):
		thisClass = Class.objects.get(pk=class_id)
		serializer = ClassSerializer(thisClass)
		return Response(serializer.data)


	def post(self):
		pass


class indBuddie(APIView):
	def get(self, request, buddie_id):
		thisbuddie = StudyBuddy.objects.get(pk=buddie_id)
		serializer = StudyBuddyserlializer(thisbuddie)
		return Response(serializer.data)

	def post():
		pass

class indGroup(APIView):
	def get(self, request, group_id):
		thisgroup = Groups.objects.get(pk=group_id)
		serializer = GroupSerializer(thisgroup)
		return Response(serializer.data)
	def post():
		pass

class indMessage(APIView):
	def get(self, request, message_id):
		thisMessage = Message.objects.get(pk=message_id)
		serializer = GroupSerializer(thisMessage)
		return Response(serializer.data)




#Returns lists of objects from database as JSON

class ClassList(APIView):
	def get(self, request):
		classes = Class.objects.all()
		serializer = ClassSerializer(classes, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class GroupList(APIView):
	def get(self, request):
		groups = Groups.objects.all()
		serializer = GroupSerializer(groups, many=True)
		return Response(serializer.data)

	def post(self):
		pass
class UserList(APIView):
	def get(self, request):
		userlist = UserBuddy.objects.all()
		serializer = UserBuddySerializer(userlist, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class StuddyBuddyList(APIView):
	def get(self, request):
		stdblist= StudyBuddy.objects.all()
		serializer = StudyBuddyserlializer(stdblist, many=True)
		return Response(serializer.data)
	def post():
		pass

class MessageList(APIView):
	def get(self, request):
		messagelist = Message.objects.all()
		serializer = MessageSerializer(messagelist, many=True)
		return JSONResponse(serializer.data)
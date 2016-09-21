from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("<h1>This is the bookup app homepage</h1>")

#lists all classes or creates a new one
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
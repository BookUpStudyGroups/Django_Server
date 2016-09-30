from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ClassSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	department = serializers.CharField(required=True, allow_blank=False, max_length=4)
	number = serializers.IntegerField()
	period = serializers.CharField(required=True, allow_blank=False,max_length=3)
	prof = serializers.CharField(required=True, allow_blank=False,max_length=20)
	title = serializers.CharField(required=True, allow_blank=False,max_length=30)
	groups = serializers.StringRelatedField(many=True, allow_empty=True)

	def create(self, validated_data):
		return Class.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.department = validated_data.get('department', instance.department)
		instance.number = validated_data.get('number', instance.number)
		instance.period = validated_data.get('period', instance.period)
		instance.prof = validated_data.get('prof', instance.prof)
		instance.title = validated_data.get('title', instance.title)
		instance.groups = validated_data.get('groups', instance.groups)
		instance.save()
		return instance


class GroupSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True, allow_blank=False, max_length=20)
	size = serializers.IntegerField()
	location = serializers.CharField(required=True, allow_blank=False, max_length=256)
	latitude = serializers.DecimalField(max_digits=7, decimal_places=6)
	longitude = serializers.DecimalField(max_digits=7, decimal_places=6)
	priv = serializers.BooleanField()
	class1 = serializers.StringRelatedField(allow_empty=True)


	def create(self, validated_data):
		return Groups.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.size = validated_data.get('size', instance.size)
		instance.location = validated_data.get('location', instance.location)
		instance.latitude = validated_data.get('latitude', instance.latitude)
		instance.longitude = validated_data.get('longitude', instance.longitude)
		instance.priv = validated_data.get('priv', instance.priv)

		instance.save()
		return instance



class UserBuddySerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	groups = serializers.StringRelatedField(many=True, allow_empty=True)
	classes = serializers.StringRelatedField(many=True, allow_empty=True)
	user = serializers.StringRelatedField(allow_empty=True)
	buddies = serializers.StringRelatedField(allow_empty = True)

	def create(self, validated_data):
		return UserBuddy.objects.create(**validated_data)

class AllStudyBuddySerializer(serializers.ModelSerializer):
	class Meta:
		model = StudyBuddy
		depth = 2
		fields = ('__all__')

	
		

class AllUserBuddySerializer(serializers.ModelSerializer):
	class Meta:
		model = UserBuddy
		depth = 1
		fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'
		depth = 2

class StudyBuddyserlializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	user1 = serializers.StringRelatedField(allow_empty=True)
	user2 = serializers.StringRelatedField(allow_empty=True)
	class1 = serializers.StringRelatedField(allow_empty=True)

class MessageSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only= True)
	date = serializers.DateTimeField()
	author = serializers.StringRelatedField(allow_empty=False)
	group = serializers.StringRelatedField(allow_empty=False)

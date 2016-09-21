from rest_framework import serializers
from .models import Class, Groups, UserBuddy
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


class GroupSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True, allow_blank=False, max_length=20)
	size = serializers.IntegerField()
	location = serializers.CharField(required=True, allow_blank=False, max_length=256)
	latitude = serializers.DecimalField(max_digits=7, decimal_places=6)
	longitude = serializers.DecimalField(max_digits=7, decimal_places=6)
	priv = serializers.BooleanField()

	def create(self, validated_data):
		return Groups.objects.create(**validated_data)

class UserBuddySerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	groups = serializers.StringRelatedField(many=True, allow_empty=True)
	classes = serializers.StringRelatedField(many=True, allow_empty=True)
	user = serializers.StringRelatedField(allow_empty=True)
	#class Meta:
	#	model = User
	#	fields = '__all__'
	def create(self, validated_data):
		return UserBuddy.objects.create(**validated_data)
class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'

class StudyBuddyserlializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	user1 = serializers.StringRelatedField(allow_empty=True)
	user2 = serializers.StringRelatedField(allow_empty=True)
	class1 = serializers.StringRelatedField(allow_empty=True)

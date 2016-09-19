from rest_framework import serializers
from .models import Class, Groups

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
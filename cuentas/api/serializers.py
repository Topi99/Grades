from rest_framework import serializers
from ..models import Profesor, Alumno, Padre
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'last_name')

class ProfesorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profesor
		fields = ('id', 'birth', 'bio', 'tel', 'user')

class PadreSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)

	class Meta:
		model = Padre
		fields = ('id', 'birth', 'bio', 'tel', 'user', 'user')
from rest_framework import serializers
from ..models import Profesor, Alumno, Padre

class ProfesorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profesor
		fields = ('id', 'birth', 'bio', 'tel', 'user')

class PadreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Padre
		fields = ('id', 'birth', 'bio', 'tel', 'user')
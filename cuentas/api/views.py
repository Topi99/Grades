from rest_framework import generics
from ..models import Profesor, Padre 
from .serializers import ProfesorSerializer, PadreSerializer

class PadreListView(generics.ListAPIView):
	queryset = Padre.objects.all()
	serializer_class = PadreSerializer
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer


class BasisModelViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

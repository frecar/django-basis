from rest_framework import viewsets
from tests.models import Person
from tests.serializers import PersonSerializer


class BasisModelViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

from rest_framework import viewsets

from .models import BasisPerson
from .serializers import PersonSerializer


class BasisModelViewSet(viewsets.ModelViewSet):
    queryset = BasisPerson.objects.all()
    serializer_class = PersonSerializer

from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import BasisPerson


class BasisModelViewSet(viewsets.ModelViewSet):
    queryset = BasisPerson.objects.all()
    serializer_class = PersonSerializer

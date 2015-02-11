from basis.serializers import BasisSerializer
from .models import Person


class PersonSerializer(BasisSerializer):
    class Meta:
        model = Person

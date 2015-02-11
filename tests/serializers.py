from basis.basis_serializer import BasisSerializer
from tests.models import Person


class PersonSerializer(BasisSerializer):
    class Meta:
        model = Person
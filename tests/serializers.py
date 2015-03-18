from basis.serializers import BasisSerializer
from .models import BasisPerson


class PersonSerializer(BasisSerializer):
    class Meta:
        model = BasisPerson

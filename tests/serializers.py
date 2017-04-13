from basis.serializers import BasisSerializer

from .models import BasisPerson


class PersonSerializer(BasisSerializer):
    class Meta:
        model = BasisPerson
        fields = ['name', 'created_by', 'updated_by']

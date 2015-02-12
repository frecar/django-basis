Usage of BasisSerializer
------------------------

Makes sure BasisModel objects created and updated have the
``created_by`` and ``updated_by`` fields set.

.. code:: python

    from basis.serializers imoprt BasisSerializer

    class PersonSerializer(BasisSerializer):
        class Meta:
            model = Person

.. py:currentmodule:: basis.serializers

.. autoclass:: BasisSerializer
    :members:

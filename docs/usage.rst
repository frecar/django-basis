Usage of TimeStampModel
-----------------------

Adds ``created_at`` and ``updated_at`` to models.

.. code:: python

    from basis.models import TimeStampModel

    class Person(TimeStampModel):
        name = models.Charfield(max_length=50)

    person = Person.objects.create(name="Fredrik"))
    print person.created_at # datetime object1

    person.name = "Rolf"
    person.save()

    print person.created_at # (datetime at the moment of the creation)
    print person.updated_at # (datetime at the moment of the update)

Usage of PersistentModel
------------------------

Safe deletion of objects.

.. code:: python

    from basis.models import PersistentModel

    class Person(PersistentModel):
        name = models.Charfield(max_length=50)

    person = Person.objects.create(name="Fredrik"))

    # SafeDelete person (safe delete)
    person.delete()

    print Person.objects.all().count() # 0 - excludes deleted users
    print Person.all_objects.all().count() # 1 - includes deleted users

    # Restore deleted person
    person = Person.all_objects.get(id=person.id)
    person.restore()

    # If you really want to delete the object
    person = Person.objects.create(name="Fredrik"))
    person.delete(force=True)

Usage of BasisModel
-------------------

Includes the functionality of both PersistentModel and TimeStampModel,
while adding the fields ``created_by`` and ``updated_by``.

.. code:: python

    from basis.models import BasisModel

    class Person(BasisModel):
        name = models.Charfield(max_length=50)

    # Save changes on objects and register who did it
    person = Person.objects.get(id=id)
    person.name = "Fredrik"
    person.save(current_user=request.user)

    # Or create a new object and register who did it
    person = Person.objects.create(name="Fredrik", current_user=request.user)

    # See meta info about the object
    print person.created_by # user object (creator)
    print person.updated_by # user object (updater)

# django-basis
[![Build status](https://ci.frigg.io/badges/frecar/django-basis/)](https://ci.frigg.io/frecar/django-basis/)
[![Coverage Status](https://coveralls.io/repos/frecar/django-basis/badge.png)](https://coveralls.io/r/frecar/django-basis)
[![PyPi version](https://pypip.in/v/django-basis/badge.png)](https://crate.io/packages/django-basis/)

## Installation
    pip install django-basis

 - Python versions: 2.6, 2.7, 3.2, 3.3
 - Support Django Customer User


## Usage of TimeStampModel

```python
from basis.models import TimeStampModel

class Person(TimeStampModel):
    name = models.Charfield(max_length=50)

person = Person.objects.create(name="Fredrik"))
print person.created_at # datetime object1

person.name = "Rolf"
person.save()

print person.created_at # (datetime at the moment of the creation)
print person.updated_at # (datetime at the moment of the update)


```


## Usage of BasisModel

```python
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
print person.created_at # (datetime at the moment of the creation)
print person.created_by # user object (creator)
print person.updated_at # (datetime at the moment of the update)
print person.updated_by # user object (updater)


# Delete person (safe_delete)
person = Person.objects.get(id=id)
person.delete()

# Restore deleted person
person = Person.all_objects.get(id=id)
person.restore()

# If you really want to delete the object
person = Person.all_objects.get(id=id)
person.delete()

```
